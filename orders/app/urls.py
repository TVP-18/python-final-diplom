from django.urls import path

from app.views import PartnerPriceLoad, CategoryView, ShopView, UserLogin, UserRegister, ProductInfoView

app_name = 'app'
urlpatterns = [
    path('user/login', UserLogin.as_view(), name='user-login'),
    path('user/register', UserRegister.as_view(), name='user-register'),
    path('partner/load', PartnerPriceLoad.as_view(), name='partner-load'),
    path('category', CategoryView.as_view(), name='category-view'),
    path('shop', ShopView.as_view(), name='shop-view'),
    path('product', ProductInfoView.as_view(), name='product-view'),
]
