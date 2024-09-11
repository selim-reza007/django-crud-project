from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('list/', views.blogsView, name='list'),
    path('new-blog/', views.NewBlogView, name='new-blog'),
    path('<int:slug>/', views.blogView, name='page'),
    path('edit/<int:slug>/', views.editView, name='edit'),
    path('delete/<int:slug>/', views.deleteView, name='delete'),
]
