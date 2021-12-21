from django.contrib.auth import authenticate
from requests import get

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from rest_framework.authtoken.models import Token

import yaml

from app.models import Category, Shop
from app.serializer import CategorySerializer, ShopSerializer


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
        url = request.data.get('url')

        print(1, request.data)
        print(2, url)


        if url:
            validate_url = URLValidator()
            try:
                validate_url(url)
            except ValidationError as e:
                return JsonResponse({'Status': False, 'Error': str(e)})
            else:
                stream = get(url).content
                print(stream)
                data = yaml.load(stream, Loader=yaml.Loader)
                print(data)
        #
                return JsonResponse({'Status': True})

        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})


class CategoryView(ListAPIView):
    """
    Просмотр категорий
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ShopView(ListAPIView):
    """
    Просмотр магазинов
    """
    queryset = Shop.objects.filter(state=True)
    serializer_class = ShopSerializer


class UserLogin(APIView):
    """
    Авторизация пользователя по логину и паролю, возвращаем токен
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