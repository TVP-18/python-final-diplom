from django.contrib.auth import authenticate
from django.db.models import Q
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from requests import get

from django.contrib.auth.password_validation import validate_password

from django.http import JsonResponse
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView


from rest_framework.authtoken.models import Token

import yaml

from app.models import Category, Shop, ProductInfo, Product, Parameter, ProductParameter
from app.serializer import CategorySerializer, ShopSerializer, UserSerializer, ProductInfoSerializer


class PartnerPriceLoad(APIView):
    """
    Загрузка/обновление прайса от поставщика
    """
    def post(self, request, *args, **kwargs):

        # проверить аутентификацию пользователя
        if not request.user.is_authenticated:
            return JsonResponse({'Status': False, 'Error': 'Пользователь не зарегистрирован'}, status=403)

        # проверить права пользователя, доступно только для магазинов
        if request.user.type != 'shop':
            return JsonResponse({'Status': False, 'Error': 'Только для магазинов'}, status=403)

        # получаем файл
        file = request.data.get('url')
        # print(request.data, file)

        if file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            # print(request.data, file, data)

            shop, _ = Shop.objects.get_or_create(name=data['shop'], user_id=request.user.id)

            for category in data['categories']:
                category_object, _ = Category.objects.get_or_create(id=category['id'], name=category['name'])
                category_object.shops.add(shop.id)
                category_object.save()

            ProductInfo.objects.filter(shop_id=shop.id).delete()
            for item in data['goods']:
                product, _ = Product.objects.get_or_create(name=item['name'], category_id=item['category'])

                product_info = ProductInfo.objects.create(product_id=product.id,
                                                          external_id=item['id'],
                                                          model=item['model'],
                                                          price=item['price'],
                                                          price_rrc=item['price_rrc'],
                                                          quantity=item['quantity'],
                                                          shop_id=shop.id)
                for name, value in item['parameters'].items():
                    parameter_object, _ = Parameter.objects.get_or_create(name=name)
                    ProductParameter.objects.create(product_info_id=product_info.id,
                                                    parameter_id=parameter_object.id,
                                                    value=value)

            return JsonResponse({'Status': True})

        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})


class CategoryView(ListAPIView):
    """
    Просмотр категорий
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    search_fields = ["name"]

    # filterset_fields = ['name']
    # # поиск по наименованию категории
    # def get_queryset(self):
    #     param = self.request.GET.get('name', None)
    #     if param:
    #         return Category.objects.filter(name__icontains=param)
    #     else:
    #         return Category.objects.all()


class ShopView(ListAPIView):
    """
    Просмотр магазинов, принимающих заказы
    """
    queryset = Shop.objects.filter(state=True)
    serializer_class = ShopSerializer

    search_fields = ['name']

    # filterset_fields = ['name']
    # # поиск по наименованию магазина
    # def get_queryset(self):
    #     param = self.request.GET.get('name', None)
    #     query = Q(state=True)
    #
    #     if param:
    #         query = query & Q(name__icontains=param)
    #
    #     return Shop.objects.filter(query)


class UserLogin(APIView):
    """
    Вход пользователя по логину и паролю, возвращаем токен
    """

    def post(self, request, *args, **kwargs):

        if {'email', 'password'}.issubset(request.data):
            user = authenticate(request, username=request.data['email'], password=request.data['password'])

            if user is not None:
                if user.is_active:
                    token, created = Token.objects.get_or_create(user=user)

                    return JsonResponse({'Status': True, 'Token': token.key})

            return JsonResponse({'Status': False, 'Errors': 'Не удалось авторизовать'})

        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})


class UserRegister(APIView):
    """
    Регистрация покупателя
    """

    def post(self, request, *args, **kwargs):

        # проверяем обязательные аргументы
        if {'first_name', 'last_name', 'email', 'password', 'company', 'position'}.issubset(request.data):
            # проверяем пароль
            try:
                validate_password(request.data['password'])
            except Exception as password_error:
                list_error = []
                for item in password_error:
                    list_error.append(item)
                return JsonResponse({'Status': False, 'Errors': {'password': list_error}})
            else:
                # проверяем структуру
                user_serializer = UserSerializer(data=request.data)
                if user_serializer.is_valid():

                    # сохраняем пользователя
                    user = user_serializer.save()
                    user.set_password(request.data['password'])
                    user.save()

                    return JsonResponse({'Status': True})
                else:
                    return JsonResponse({'Status': False, 'Errors': user_serializer.errors})

        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})


class ProductInfoView(ListAPIView):
    serializer_class = ProductInfoSerializer
    queryset = ProductInfo.objects.all()
# class ProductInfoView(APIView):
#     """
#     Список продуктов
#     """
#
    # def get(self, request, *args, **kwargs):
    #
    #     query = Q(shop__state=True)
    #     shop_id = request.query_params.get('shop_id')
    #     category_id = request.query_params.get('category_id')
    #
    #     if shop_id:
    #         query = query & Q(shop_id=shop_id)
    #
    #     if category_id:
    #         query = query & Q(product__category_id=category_id)
    #
    #     # фильтруем и отбрасываем дуликаты
    #     queryset = ProductInfo.objects.filter(
    #         query).select_related(
    #         'shop', 'product__category').prefetch_related(
    #         'product_parameters__parameter').distinct()
    #
    #     serializer = ProductInfoSerializer(queryset, many=True)
    #
    #     return Response(serializer.data)