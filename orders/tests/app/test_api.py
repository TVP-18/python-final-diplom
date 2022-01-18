import pytest
from django.urls import reverse

from app.models import Category, Shop, Contact


@pytest.mark.django_db
def test_category_get(api_client, category_factory):
    """
    Список категорий
    """
    url = reverse('app:category-view')
    category_factory(_quantity=5)
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 5


@pytest.mark.django_db
def test_shop_get(api_client, shop_factory):
    """
    Список магазинов
    """
    url = reverse('app:shop-view')
    shop_factory(_quantity=5)
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 5


@pytest.mark.django_db
def test_contact_post_by_anonymous_user(api_client):
    """
    Анонимный пользователь пытается добавить новый контакт
    """
    payload = {"city": "Город 1", "street": "Улица 1", "house": "1", "structure": "1",
               "building": "1", "apartment": "1", "phone": "11111111"}
    url = reverse('app:user-contact')
    response = api_client.post(url, data=payload)
    assert response.status_code == 403
