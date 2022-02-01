from api import views
from django.urls import path
from rest_framework.routers import DefaultRouter

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
