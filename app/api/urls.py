from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

app_name = 'api'

urlpatterns = [
    path('catalogs/', views.CatalogsView.as_view(),
         name='catalogs'),
    path('experiences/', views.ListExperiencesView.as_view(),
         name='experiences'),
    path('experiences/<str:id>/', views.ExperiencesView.as_view(),
         name='experience'),
]
