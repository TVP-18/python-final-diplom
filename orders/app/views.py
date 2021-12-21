from requests import get

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

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
