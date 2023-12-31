from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('<int:user_pk>/password/', views.change_password, name='change_password'),
    path('profile/<username>/', views.profile, name='profile'),
    path('<int:user_pk>/follow', views.follow, name='follow'),
    path('<int:user_pk>/likedmovielist/', views.likedmovielist, name = 'likedmovielist'),
    path('<int:user_pk>/followerlist/', views.followerlist, name='followerlist'),
    path('<int:user_pk>/followinglist/', views.followinglist, name='followinglist'),
]