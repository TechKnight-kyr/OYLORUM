
from django.shortcuts import render, redirect
from .models import Article, comment
from django.urls import reverse
from django.views.generic.base import View
from django.http import Http404, HttpResponseRedirect
from django.utils import timezone
from .form  import ArticleForm, UserLoginForm, UserRegistrationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Article


from django.shortcuts import get_object_or_404

@login_required
def my_profile(request):
    # Берем статьи только текущего юзера
    user_articles = Article.objects.filter(author=request.user).order_by('-pub_date')
    return render(request, 'articles/profile.html', {'user_articles': user_articles})

@login_required
def delete_article(request, article_id):
    # Находим статью или выдаем 404. 
    # filter(author=request.user) гарантирует, что чужую статью удалить нельзя!
    article = get_object_or_404(Article, id=article_id, author=request.user)
    if request.method == "POST":
        article.delete()
    return redirect('articles:profile')
@login_required
def add_article(request):
    if request.method == "POST":
        title = request.POST.get('art_title') 
        text = request.POST.get('art_text')
        image = request.FILES.get('image_file') 

        new_article = Article(
            article_title=title,  
            article_text=text,
            image=image,            
            author=request.user,    
            pub_date=timezone.now()
        )
        new_article.save()
        return redirect('articles:index') 

    return render(request, 'articles/page1.html')


def begin(request):
	articles_list = Article.objects.all()
	return render(request, 'articles/list.html', {'articles_list':articles_list})



def index(request):
	latest_articles_list = Article.objects.order_by('-pub_date')[:5]
	article_list1 = Article.objects.all()

	return render(request, 'articles/begin.html', {'article_list1':article_list1})



def detail(request, article_id):
	try:
		a = Article.objects.get( id = article_id )
	except:
		raise Http404('Статья не найдена')

	latest_comments_list = a.comment_set.order_by('-id')[:10]

	return render(request, 'articles/detail.html',{'article':a, 'latest_comments_list':latest_comments_list })

def leave_comment(request, article_id):
    a = Article.objects.get(id=article_id)
    
    if request.method == "POST":
        if request.user.is_authenticated:
            # Если вошел — берем его имя
            full_name = request.user.username
        else:
            # Если не вошел — всегда "Гость"
            full_name = "Гость"
        
        # Сохраняем комментарий
        a.comment_set.create(
            author_name=full_name,
            comment_text=request.POST.get('text')
        )
        
    return redirect('articles:detail', article_id=a.id)
        
    return redirect('articles:detail', article_id=a.id)


def leave_artc(request):
    if request.method == 'POST': 
        print('beginning is okay')
        article_title1 = request.POST.get('art_title')
        article_text1 = request.POST.get('art_text')
        image = request.FILES.get('image_file')
        print('creating info is okay')
        pub_date1 = timezone.now()
        article = Article.objects.create(article_title=request.POST['art_title'], 
        	article_text=request.POST['art_text'], 
        	image=request.FILES['image_file'],
        	author= request.user, 
        	 pub_date=timezone.now())
        article.save()
        return redirect('/')
    else:
        raise Http404('Статья не найдена')


def login(request):
	print('begin is okey')
	if request.method == 'POST':
		print('1if is okey')
		form = UserLoginForm(data=request.POST)
		print('1.5if is okey')
		print(form.errors)
		if form.is_valid():
			print(form.errors)
			print('3if is okey')
			user_name = request.POST['username']
			password = request.POST['password']
			print('3.4if is okey')
			user  = auth.authenticate(username=user_name, password=password)
			
			if user:
				print('4if is okey')
				auth.login(request, user)
				#return HttpResponseRedirect(reverse('begin'))
				return HttpResponseRedirect('/')
				#return redirect('././list.html')

	else:
		form = UserLoginForm()
		print('else is okey')


	context = {'form': form}
	return render(request, 'articles/login.html', context)


def registration(request):
	print('1begin is okey')

	if request.method == 'POST':
		print('begin is okey')
		form = UserRegistrationForm(data = request.POST)
		print('begin2 is okey')
		if form.is_valid():
			save = form.save(commit=False)
			save.save()
			print('valid is okey')
			return redirect('/login')

	else:
		form = UserRegistrationForm()
	context = {'form':form}
	return render(request, 'articles/registration.html', context)




