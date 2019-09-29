"""DjangoBaseFrame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib.auth import views as auth_views
from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    #user space redirects
    path('', include('start_page_app.urls')),
    path('user/', include('user_space_app.urls')),

    #user access redirects
    path('signup/', include('user_access_app.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='user_access_app/login.html'), name='login_page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user_access_app/logout.html'), name='logout_page'),
    
    #password reset redirects:
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_management_app/password_reset.html'), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_management_app/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_management_app/password_reset_complete.html'), name='password_reset_complete'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_management_app/password_reset_done.html'), name='password_reset_done')
]
