from django.shortcuts import render,redirect,get_object_or_404
from .forms import TweetForm
from .models import Tweet

# Create your views here.


def index(req):
    return render(req,'index.html')

def TweetRead(req):
    tweets=Tweet.objects.all()
    return render(req,'tweets.html',{'tweets':tweets})


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

def  TweetDelete(req,id):
    tweet=get_object_or_404(Tweet,pk=id,user=req.user)
    if req.method=='POST':
        tweet.delete()
        return redirect('ReadTweets')
    return render(req,'tweet_confirm_delete.html',{'tweet':tweet})
