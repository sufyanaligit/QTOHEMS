# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView, UserProfileView, UserLoginView,ProjectViewSet,ContactUsListCreate,create_quote_request

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('drflogin/', UserLoginView.as_view(), name='user-login'),
    path('create-quote/', create_quote_request.as_view(), name='create_quote_request'),
    path('create-contact/', ContactUsListCreate.as_view(), name='create_contact_us'),
    path('projects/', include(router.urls)),
]
 