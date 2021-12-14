from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

app_name = 'api'

urlpatterns = [
    path('catalogs/', views.CatalogsView.as_view(),
         name='catalogs'),
    path('experiences/', views.list_experiences,
         name='experiences'),
    path('experiences/<str:id>/', views.experience,
         name='experience'),
]
