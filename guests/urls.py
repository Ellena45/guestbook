
from . import views
from django.urls import path
from .views import UserList, UserDetail, UserCreate, UserUpdate, DeleteView, CustomLoginView, UserLeave, UserLogout, Impressum
from django.contrib.auth.views import LogoutView

app_name = 'guests'
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='guests:login'), name='logout'),
    path('', UserList.as_view(), name='users'),
    path('user/<int:pk>/', UserDetail.as_view(), name='user'),
    path('user-create/', UserCreate.as_view(), name='user-create'),
    path('user-update/<int:pk>/', UserUpdate.as_view(), name='user-update'),
    path('user-delete/<int:pk>/', DeleteView.as_view(), name='user-delete'),
    path('user-leave/', UserLeave.as_view(), name='user-leave'),
    path('user-logout/<int:pk>/', UserLogout.logout, name='user-logout'),
    path('user-impressum/', Impressum.as_view(), name='user-impressum'),
    path('export/csv-database-write/', views.csv_database_write, name='csv_database_write'),
]