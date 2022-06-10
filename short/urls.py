from django.urls import path
from short import views

from short.views import (
    HomeView, 
    UrlCreateView, 
    UrlDeleteView, 
    UrlDetailView, 
    UrlListView, 
    UrlUpdateView
)

urlpatterns = [
    # path('',HomeView.as_view(),name='home'),
    path('',views.CreateShortUrl, name = 'create'),
    path('new',views.NewShortUrl,name='url-show'),
    path('url',UrlListView.as_view(),name='url-list'),
    path('url/<int:pk>/',UrlDetailView.as_view(),name='url-detail'),
    path('url/<int:pk>/update',UrlUpdateView.as_view(),name='url-update'),
    path('url/<int:pk>/delete',UrlDeleteView.as_view(),name='url-delete'),

]
