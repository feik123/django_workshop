from django.urls import path

from authors import views

urlpatterns = [
    path('create/', views.CreateAuthorPage.as_view(), name='author-create'),
]