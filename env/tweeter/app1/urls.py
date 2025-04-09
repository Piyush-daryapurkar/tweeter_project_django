from django.urls import path

from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('read/',views.TweetRead,name='ReadTweets'),
    path('add/',views.TweetAdd, name='add')
]