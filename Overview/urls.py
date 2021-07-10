from django.contrib import admin
from django.urls import path, re_path
from .views import *
app_name = "Mona"
admin.autodiscover()
urlpatterns = [
    path('', homepage, name="homepage"),
    path('product/', ProductDetailView.as_view()),
    path('logged_in', logged_in, name="logged_in"),
    path('register', register, name="register"),
    path('create-product', ProductCreateView.as_view(), name="create-product"),
    path('detail/<int:id>', detail, name="detail"),
    path('login_view', login_view, name="login_view"),
    path('login', login_page, name="login_page"),
    path('add_comment/<int:id>', add_comment, name="add_comment"),    
    path('form', tryform, name='form'),
    path('get_comments', get_comments, name="get_comments"),
]
