from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import Article,NewsLetterRecipients
from .forms import NewsLetterForm,  NewArticleForm
from .email import send_welcome_email  #-----import send_welcome_email and call it after validation
from django.contrib.auth.decorators import login_required

# -----------------------------------------------first we import NewsletterForm
from .forms import NewArticleForm, NewsLetterForm


# Create your views here.

def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()
#----------------------------------------we use post method because the form is submitting data to database  
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():   #----checks if form is validated
            print('valid')
            # After form validation, the name and email are saved in cleaned_data property-a dictionary 
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            
            # recipient variable retrives name and email
            recipient = NewsLetterRecipients(name = name,email =email)
            # name and email saved
            recipient.save()
            send_welcome_email(name,email)  #-----import send_welcome_email and call it after validation
            
            
            #redirect the user back to the news_today view function.
            
            HttpResponseRedirect('news_today')
    else: #--------------------------------if the form is not valid, just create an empty form instance and pass it to template
        form = NewsLetterForm()
    
    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY

    return render(request, 'all-news/today-news.html', {"date": date,"news":news, "letterForm":form})



#View function to present news from past days
def past_days_news(request,past_date):
    
    try:    
        # Converts data from the string url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    
    except ValueError:
        #Raise 404 error when ValueError is thrown
        raise Http404
        assert False
        
    if date ==dt.date.today():
        return redirect(news_today)
    news = Article.days_news(date)
    return render(request, 'all-news/past-news.html', {"date":date,"news":news})
def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"
   
        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})
    
@login_required(login_url='/accounts/login/')
def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html", {"article":article})


@login_required(login_url='/accounts/login/')
def new_article(request): #new function thst calls the form
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)  #the request.FILES arguement is passed in because we are going to be uploading an image file and we want to process it in our form 
        if form.is_valid(): #validating the form
            article=form.save(commit=False)  #if the form is valid, we save it using the save() method. #we pass in the commit=False to prevent it from saving to the database.
            article.editor = current_user #here we are setting the editor attribute to the current user
            article.save()
        return redirect('NewsToday')
    else:
        form = NewArticleForm()
    return render(request, 'new_article.html', {"form":form})
