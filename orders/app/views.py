from requests import get

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from yaml import load, Loader

from app.models import Category
from app.serializer import CategorySerializer


class PartnerPriceLoad(APIView):
    """
    Класс для загрузки/обновления прайса от поставщика
    """
    def post(self, request, *args, **kwargs):
        # проверить аутентификацию пользователя

        # проверить права пользователя, доступно только для магазинов

        # получаем файл
        url = request.data.get('url')
        # print(request, request.data, url)
        if url:
            validate_url = URLValidator()
            try:
                validate_url(url)
            except ValidationError as e:
                return JsonResponse({'Status': False, 'Error': str(e)})
            else:

                stream = get(url).content
                print(stream)
                data = load(stream, Loader=Loader)
                print(data)

                return JsonResponse({'Status': True})

        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})


class CategoryView(ListAPIView):
    """
    Класс для просмотра категорий
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


