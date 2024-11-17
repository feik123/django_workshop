from django.urls import path, include

from posts import views

urlpatterns = [
    path('create/', views.CreatePost.as_view(), name='post-create'),
    path('<int:post_id>/', include([
        path('details/', views.PostDetails.as_view(), name='post-details'),
    ]))
]