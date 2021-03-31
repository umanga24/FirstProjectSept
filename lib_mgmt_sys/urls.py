from django.urls import path
from lib_mgmt_sys import views

app_name = 'lms'

urlpatterns = [
    path('list_books/', views.list_books, name = 'list_books'),
    path('add_books/', views.add_books, name = 'add_books'),
    path('edit_book/<int:id>/', views.edit_book, name= 'edit_book'),
    path('delete_book/<int:id>/', views.delete_book, name = 'delete_book'),
    path('add_author/', views.add_author, name= 'add_author'),
    path('list_author/', views.list_author, name= 'list_authors'),
    path('edit_author/<int:id>/', views.edit_author, name= 'edit_author'),
    path('delete_author/<int:id>/', views.delete_author, name = 'delete_author'),
    path('list_student/', views.StudentListView.as_view(), name = 'list_student'),
    path('add_student/', views.StudentAddView.as_view(), name = 'add_student'),
    path('edit_student/<int:pk>/', views.StudentEditView.as_view(), name = 'edit_student'),
    path('detail_student/<int:pk>/', views.StudentDetailView.as_view(), name = 'detail_student'),
    path('delete_student/<int:pk>/', views.StudentDeleteView.as_view(), name = 'delete_student'),

    path('login/', views.loginUserView.as_view(), name = 'login_user'),
    path('logout/', views.LogoutUserView.as_view(), name = 'logout'),
    path('register/', views.RegisterUserView.as_view(), name = 'register'),

    path('book_api/', views.CsrfBookAPI, name = 'books_api'),
    path('book_api/<int:id>/', views.CsrfBookObjectAPI, name = 'book_api')
]