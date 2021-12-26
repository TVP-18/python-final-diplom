## Примеры запросов к API 

#### Регистрация пользователя
```
POST /api/v1/user/register
{
    "email": "mail@test.org"
    "first_name": "Jhon",
    "last_name": "Smith",
    "password": "fsjfkl12!",
    "company": "My Dog",
    "position": "Manager"
}

200 OK
```

#### Получение токена
```
POST /api/v1/user/login
{
    "email": "mail@test.org"
    "password": "fsjfkl12!",
}

200 OK
{
    "token": "b39d0f93f9e895b82f1724832b7c186a",
}
```

#### Обновление прайса поставщиком
```
POST /api/v1/partner/load
Authorization: Token 05b0897fc95950b403f0f81330d3fdb63c4ab960
{
    "url": "https://partner-site.ru/files/price.yaml"
}

200 OK
```

#### Список категорий
```
GET /api/v1/category

Поиск по наименованию - задать параметр search 
GET /api/v1/category?search=смарт

200 OK
[
    {
        "id": 224,
        "name": "Смартфоны"
    },
    {
        "id": 15,
        "name": "Аксессуары"
    }
]
```
#### Список магазинов, предоставляющих услуги
```
GET /api/v1/shop

Поиск по наименованию - задать параметр search 
GET /api/v1/shop?search=связ

200 OK
[
    {
        "id": 1,
        "name": "Связной",
        "url": null,
        "state": true
    }
]
```
#### Список продуктов
```
GET /api/v1/product

Поиск по наименованию или модели - задать параметр search 
GET /api/v1/product?search=xr

Фильтр по магазину и категории
GET /api/v1/product?shop_id=123&category_id=987

200 OK
[
    {
        "id": 1,
        "model": "apple/iphone/xs-max",
        "product": {
            "id": 1,
            "name": "Смартфон Apple iPhone XS Max 512GB (золотистый)"
        },
        "shop": 1,
        "quantity": 14,
        "price": 110000,
        "price_rrc": 116990,
        "product_parameters": [
            {
                "parameter": "Диагональ (дюйм)",
                "value": "6.5"
            },
            {
                "parameter": "Разрешение (пикс)",
                "value": "2688x1242"
            },
            {
                "parameter": "Встроенная память (Гб)",
                "value": "512"
            },
            {
                "parameter": "Цвет",
                "value": "золотистый"
            }
        ]
    }
]
```