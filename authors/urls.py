from django.urls import path

from authors import views

urlpatterns = [
    path('create/', views.CreateAuthor.as_view(), name='author-create'),
    path('details/', views.AuthorDetails.as_view(), name='author-details'),
]