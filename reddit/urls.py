from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('create-post', views.PostCreate.as_view(), name='create_post'),
    path('edit/<slug:slug>', views.UpdatePost.as_view(), name='update_post'),
    path('delete/<slug:slug>', views.DeletePost.as_view(), name='delete'),
    path('user-profile', views.ProfilePostList.as_view(), name='user_profile')
    ]