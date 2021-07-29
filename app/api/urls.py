from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

app_name = 'api'

urlpatterns = [
    path('catalogs/', views.catalogs),
    path('experiences/', views.list_experiences,
         name='experiences'),
    path('experiences/<str:course_id>/', views.experience,
         name='experience'),
]
