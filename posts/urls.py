from django.urls import path, include

from posts import views

urlpatterns = [
    path('create/', views.CreatePost.as_view(), name='post-create'),
    path('<int:post_id>/', include([
        path('details/', views.PostDetails.as_view(), name='post-details'),
        path('edit/', views.PostEdit.as_view(), name='post-edit'),
        path('delete/', views.PostDelete.as_view(), name='post-delete'),
    ]))
]