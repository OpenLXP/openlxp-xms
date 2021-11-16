from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import RegisterView, LoginView, LogoutView

# define the router
router = DefaultRouter()

# define the app name
app_name = 'users'

# url patterns
urlpatterns = [
    path('auth/', include(router.urls)),
    path('auth/register', RegisterView.as_view(), name='register'),
    path('auth/login', LoginView.as_view(), name='login'),
    path('auth/logout', LogoutView.as_view(), name='logout'),
]
