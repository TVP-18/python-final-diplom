from django.contrib import admin

# Register your models here.
from app.models import Shop, Category, Product, ProductInfo, Parameter, ProductParameter, \
    Order, OrderItem, Contact


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductInfo)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Parameter)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductParameter)
class CategoryAdmin(admin.ModelAdmin):
    pass

