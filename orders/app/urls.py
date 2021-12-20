from django.urls import path

from app.views import PartnerPriceLoad

app_name = 'app'
urlpatterns = [
    path('partner/load', PartnerPriceLoad.as_view(), name='partner-load'),

]
