from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from app.models import User, Shop, Category, Product, ProductInfo, Parameter, ProductParameter, \
    Order, OrderItem, Contact


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Панель управления пользователями
    """
    model = User

    fieldsets = (
        (None, {'fields': ('email', 'password', 'type')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'company', 'position')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')


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

