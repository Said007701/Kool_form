from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('password/',views.password,name='password'),
    path('pages/',views.pages,name='pages'),
    path('contact/',views.contact,name='contact'),
    path('list/',views.list,name='list'),
    path('create/', views.Create,name='Create' ),
    path('list/',views.list_book, name='list_book'),
    path('update/<int:list_id>/', views.update_book,name='update_book'),
    path('delete/<int:list_id>/', views.delete_book,name='delete_book')
]