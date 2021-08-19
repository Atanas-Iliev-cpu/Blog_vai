from django.urls import path

from blog_vai.accounts.views import RegisterView, LogInView, logout_user, ProfileDetailsView, UsersListView, \
    MyAllBlogsView, FavBlogsListView, AccountDeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register user'),
    path('login/', LogInView.as_view(), name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('profile/', ProfileDetailsView.as_view(), name='profile details'),
    path('all_users/', UsersListView.as_view(), name='all users'),
    path('my_blogs/<int:pk>', MyAllBlogsView.as_view(), name='my blogs'),
    path('fav_blogs/<int:pk>', FavBlogsListView.as_view(), name='fav blogs'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete account'),
]
