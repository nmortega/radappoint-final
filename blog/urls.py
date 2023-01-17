from django.urls import path
from .views import PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, PostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('booking/new/', PostCreateView.as_view(), name='post-create'),
    path('booking/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('booking/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('booking/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    # path('booking/', views.booking, name='blog-booking')

]
