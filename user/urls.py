from django.urls import path
from .views import profile, beneficiary, update, delete, create
from user import views as user_view
from django.contrib.auth import views as auth_views
from .api import test_list, users_list
from two_factor.views import LoginView


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    # path('', auth_views.LoginView.as_view(template_name='two_factor/core/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'),
    path('register/',user_view.register, name='user-register'),
    path('profile/', profile, name='profile'),
    path('testapi/', test_list, name='apitest'),
    path('usersapi/', users_list, name='users_list'),
    path('profile/beneficiary/', beneficiary, name='beneficiary'),
    path('profile/beneficiary/create/', create, name='create-beneficiary'),
    path('profile/beneficiary/update/<int:pk>/', update, name='update-beneficiary'),
    path('profile/beneficiary/delete/<int:pk>/', delete, name='delete-beneficiary'),
    path('userform/', user_view.generate_pdf, name='er-form'),
    # path('userform/', user_view.memberform, name='erorm'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),

]
