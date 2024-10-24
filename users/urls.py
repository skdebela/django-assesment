from django.urls import path, include
from users.views import UserDetailView

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('auth/social/', include('allauth.socialaccount.urls')),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]
