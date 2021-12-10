from django.urls import include, path

from rest_framework.routers import DefaultRouter


# define the router
router = DefaultRouter()

# define the app name
app_name = 'users'

# url patterns
urlpatterns = [
    path('auth/', include(router.urls)),
]
