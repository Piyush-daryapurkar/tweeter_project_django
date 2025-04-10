from django.urls import path

from .import views
urlpatterns = [
    path('',views.TweetRead,name='ReadTweets'),
    path('add/',views.TweetAdd, name='add'),
    path('like/<int:tweet_id>/', views.like_tweet, name='like_tweet'),
    path('delete/<int:id>/', views.TweetDelete, name='tweetDelete'),
    path('<int:id>/edit/',views.TweetEdit,name='Edit'),
    path('register/',views.register,name='register')

]