from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse

from .forms import TweetForm,UserRegistrationForm
from .models import Tweet
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.



def TweetRead(req):
    tweets=Tweet.objects.all()
    return render(req,'tweets.html',{'tweets':tweets})

@login_required
def TweetAdd(req):
    if req.method=='POST':
        form=TweetForm(req.POST , req.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=req.user
            tweet.save()
            return redirect('ReadTweets')
    else:
        form=TweetForm()
        return render(req,'tweetAdd.html',{'form':form})
        

@login_required
def TweetEdit(req,id):
    tweet=get_object_or_404(Tweet,pk=id,user=req.user)
    if req.method=="POST":
        form=TweetForm(req.POST,req.FILES,instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=req.user
            tweet.save()
            return redirect('ReadTweets')
    else:
        form=TweetForm(instance=tweet)
        return render(req,'tweetEdit.html',{'form':form})  
@login_required
def  TweetDelete(req,id):
    tweet=get_object_or_404(Tweet,pk=id,user=req.user)
    if req.method=='POST':
        tweet.delete()
        return redirect('ReadTweets')
    return render(req,'tweetDelete.html',{'tweet':tweet})


@login_required
def like_tweet(request, tweet_id):
    if request.method == "POST":
        tweet = Tweet.objects.get(id=tweet_id)
        tweet.like_count += 1
        tweet.save()
        return JsonResponse({'like_count': tweet.like_count})

    
def register(req):
    if req.method=="POST":
        form=UserRegistrationForm(req.POST)
        if form.is_valid():
            user=form.save()
            return redirect('ReadTweets')
    else:
        form = UserRegistrationForm()
        return render(req,'registration/register.html',{'form':form})    