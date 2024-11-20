from django.urls import path

from authors import views

urlpatterns = [
    path('create/', views.CreateAuthor.as_view(), name='author-create'),
    path('details/', views.AuthorDetails.as_view(), name='author-details'),
    path('edit/', views.AuthorEdit.as_view(), name='author-edit'),
    path('delete/', views.AuthorDelete.as_view(), name='author-delete'),
]