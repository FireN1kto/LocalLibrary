from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    re_path(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    re_path(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout'),
    re_path(r'^accounts/register/$', views.RegisterView.as_view(), name='register'),
    re_path(r'^accounts/register/done/$', views.RegisterDoneView.as_view(), name='register-done'),
]