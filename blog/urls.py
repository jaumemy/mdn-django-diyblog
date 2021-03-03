from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers/', views.BlogAuthorListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>', views.BlogAuthorDetailView.as_view(), name='blogger-detail'),
    path('blog/<int:pk>/comment/', views.BlogCommentCreate.as_view(), name='blog-comment'),
]
