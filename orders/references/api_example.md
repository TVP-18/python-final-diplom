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

#### Список магазинов, предоставляющих услуги
```
GET /api/v1/category?name=ар

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
#### Список категорий
```
GET /api/v1/category?name=связ

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
