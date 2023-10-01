from django.urls import path,include
from .views import (UserRegistrationView,
                    UserLoginView,
                    ProfileView,
                    ChangePasswordView,
                    PasswordResetEmailView,
                    UserPasswordResetView,)

urlpatterns=[
    path('register/', UserRegistrationView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('profile/', ProfileView.as_view(),name='profile'),
    path('passchange/', ChangePasswordView.as_view(), name='password-change'),
    path('send_pass_reset_link/',PasswordResetEmailView.as_view(),name='reset_pass_link_to_email'),
    path('reset_password/<uid>/<token>/',UserPasswordResetView.as_view(),name='reset_view')
]