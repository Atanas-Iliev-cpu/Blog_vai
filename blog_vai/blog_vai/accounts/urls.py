from django.urls import path

from blog_vai.accounts.views import RegisterView, LogInView, logout_user, ProfileDetailsView, UsersListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register user'),
    path('login/', LogInView.as_view(), name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('profile/', ProfileDetailsView.as_view(), name='profile details'),
    path('all_users/', UsersListView.as_view(), name='all users'),
]
