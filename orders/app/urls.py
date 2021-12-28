from django.urls import path

from app.views import PartnerPriceLoad, CategoryView, ShopView, UserLogin, UserRegister, ProductInfoView, \
    PartnerOrdersView, BasketView, ContactView


app_name = 'app'
urlpatterns = [
    path('user/login', UserLogin.as_view(), name='user-login'),
    path('user/register', UserRegister.as_view(), name='user-register'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('user/basket', BasketView.as_view(), name='basket'),
    path('partner/load', PartnerPriceLoad.as_view(), name='partner-load'),
    path('partner/orders', PartnerOrdersView.as_view(), name='partner-orders'),
    path('category', CategoryView.as_view(), name='category-view'),
    path('shop', ShopView.as_view(), name='shop-view'),
    path('product', ProductInfoView.as_view(), name='product-view'),

]
