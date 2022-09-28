from django.urls import path
from . import views

app_name = 'App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blogs'),
    path('add_blog/', views.AddBlog.as_view(), name='add_blog'),
    path('details/<slug:blog_slug>/', views.BlogDetail, name='blog_detail'),
]