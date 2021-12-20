from django.urls import path

from app.views import PartnerPriceLoad, CategoryView

app_name = 'app'
urlpatterns = [
    path('partner/load', PartnerPriceLoad.as_view(), name='partner-load'),
    path('category', CategoryView.as_view(), name='category-view'),
]
