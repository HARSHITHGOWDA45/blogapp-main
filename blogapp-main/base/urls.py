from django.urls import path
from . import views
from .views import PostListView,PostDetailedView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),

    # Create must come before <str:username>
    path('post/new/', PostCreateView.as_view(), name='post_create'),

    # Specific post detail (int:pk) must come before <str:username>
    path('post/<int:pk>/', PostDetailedView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # Username path should always come last
    path('post/<str:username>/', UserPostListView.as_view(), name='user_post'),

    path('about/', views.about, name='about'),
]


# urlpatterns=[
#     path('',PostListView.as_view(),name='home'),
#     path('post/new/',PostCreateView.as_view(),name='post_create'),
#     path('post/<str:username>/',UserPostListView.as_view(),name='user_post'),
#     path('post/<int:pk>/',PostDetailedView.as_view(),name='post_detail'),
#     path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post_update'),
#     path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post_delete'),
#     path('about/',views.about,name='about')
# ]