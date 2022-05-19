from django.urls import path
from . import views

urlpatterns = [
    path('', views.CompaniesList.as_view(), name='companies_list'),
]
