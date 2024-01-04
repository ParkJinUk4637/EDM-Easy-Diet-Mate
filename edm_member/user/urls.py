from django.urls import path, include
from . import views
from rest_framework import urls
from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib.auth.views import PasswordResetConfirmView

urlpatterns =[
    path('user/', views.CreateUser.as_view()), # 유저 생성
    path('login/', views.Login.as_view(),), # 로그인
    path('auth/refresh/',TokenRefreshView.as_view()), # access 토큰 재발급
    path('user/info/',views.user_info), # 유저 정보 조회, 수정, 삭제
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'), # 개인정보 처리방침 조회
    path('check-email-existence/', views.check_email_existence, name='check_email_existence'),
    path('password-reset/',views.PasswordResetView.as_view(),name='password-reset'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('api-auth/', include('rest_framework.urls')),
]