from django.urls import path
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('signin/', views.login_page, name='signin'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('user_change/', views.user_change, name='user_change'),
    path('password/', views.password_change, name='change_pass'),
    path('change_profile/', views.add_pro_pic, name='add_profile_pic'),
    path('change_profile_picture/', views.change_pro_pic, name='change_profile_pic'),

]

