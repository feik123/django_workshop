from django.urls import path

from authors import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
]