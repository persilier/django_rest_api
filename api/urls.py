from django.urls import path
from . import views

urlpatterns = [
    path('blogposts/', views.BlogPostLisCreate.as_view(),name='blogpost-list-create'),
    path('blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(),name='blogpost-retrieve-update-destroy'),
]


