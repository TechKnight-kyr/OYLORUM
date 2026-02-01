
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User
class Article(models.Model):
	article_title = models.CharField('name of title', max_length=200)
	article_text = models.TextField('text of article')
	pub_date = models.DateTimeField('date of publication')
	image = models.ImageField(upload_to='articles_pics/', blank=True, null=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

	def __str__(self):
		return self.article_title

	def was_published_recently(self):
			return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'

class comment(models.Model):
	article =models.ForeignKey(Article, on_delete = models.CASCADE)
	author_name = models.CharField('name of author', max_length=50)
	comment_text = models.CharField('text of comment', max_length=300)


	def __str__(self):
		return self.author_name

	class Meta:
		verbose_name = 'Коментарии'
		verbose_name_plural = 'Коментарии'



'''
	user_name = models.CharField(max_length=40, null=True)
	user_email = models.EmailField()
	password = models.CharField('Ваш пароль', max_length=50)
#	first_name = models.CharField('first_name', max_length=40, null=True)
#	last_name = models.CharField('last_name', max_length=40, null=True)
#	password2 = models.CharField('password2', max_length=50, null=True)
	objects = UserManager()

	USERNAME_FIELD = "user_name"

	def __str__(self):
		return self.user_name
	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'
'''




exp_models = '''
user_name = models.CharField('Ваше имя', max_length=70, unique=True)

class User(AbstractBaseUser):
    uid = models.UUIDField(
        default=None,
        blank=True,
        null=True,
        unique=True,
    )
class MyUser(AbstractBaseUser):
    identifier = models.CharField(max_length=40, unique=True)
    ...
    USERNAME_FIELD = "identifier"

from articles.models import Article, comments - это метод для того чтобы управлять базой данных
но можно это сделать также как у Ивана Викторовича но до первого момента нужно импортировать консоль пайтона
python manage.py shell

Article.objects.filter(article_title_startswith = "Какая") - это специальный фильтр позволяющтй 
сфильтровать данные базе данных 

a = Article.objects.get(id = 1)  - это метод для того чтобы сделать екземпляр базы данных а дальше и 
манипулировать с ней 'Article' - это название базы данных а id = 1 - это айди статьи в базе данных
a.save() - после изменений нужно обезательно сохранить 

a.article_title = "Какаши хатаке" - это метод для того чтобы изменить данные в article_title
title - можно менять смотря на отделы в базе данных

a.comment_set.filter(author_name__startswith = "s") - метод чтобы отфильтровать сообщения

УДАЛЕНИЕ ОБЬЕКТА  ИЗ БАЗЫ ДАННЫХ
cs = a.comment_set.filter(author_name__startswith = 'm')  
cs.delete() 

	class Meta:
		verbose_name = 'Коментарии'
		verbose_name_plural = 'Коментарии' - это специальный метод позволяющий выдавать иное название моделей
		Article -- Статья

	{% if latest_articles_list %}

		{% else %}
		Статьи не найдены
	{% endif %}]


class Article(models.Model):
	article_title = models.CharField('name of title', max_length=200)
	article_text = models.TextField('text of article')
	pub_date = models.DateTimeField('date of publication')

	def __str__(self):
		return self.article_title

	def was_published_recently(self):
			return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'

class comment(models.Model):
	article =models.ForeignKey(Article, on_delete = models.CASCADE)
	author_name = models.CharField('name of author', max_length=50)
	comment_text = models.CharField('text of comment', max_length=300)


	def __str__(self):
		return self.author_name

	class Meta:
		verbose_name = 'Коментарии'
		verbose_name_plural = 'Коментарии'

		<a href="{% url 'articles:detail' test.id %}"><{{test.article_title}}</a>
		<h2>{{test.article_title}}</h2>
		<a href="{% url 'articles:detail' test.id %}"><{{test.article_title}}</a>
<hr>

<form action="{% url 'articles:leave_artc' %}" method="POST">

	{% csrf_token %}

	<input type="text" required placeholder="название статьи" name="art_title"><br>
	<textarea name="art_text" required="" placeholder="текст статьи" cols="30" rows="10"></textarea><br>

	<button type="submit">сохранить статью</button>

</form>
<p><a href="/page1" class="active">назад</a></p>
<li><a href="/page1" class="active">Статьи</a></li>

	{% for test in article_list1 %}
		<a href="{% url 'articles:detail' test.id %}">{{test.article_title}}</a>
		<p><h4>{{test.article_text}}</h4></p>   <h4>{{test.pub_date}}</h4>
	{% endfor %}



	<div class="form-group">
		<label class="small mb-1" for="inputEmailAddress">Имя пользователя</label>
		<input class="form-control py-4" id="inputEmailAddress" type="text" placeholder="Введите имя пользователя"/>
	</div>
	<div class="form-group">
    	<label class="small mb-1" for="inputPassword">Пароль</label>
   	 <input class="form-control py-4" id="inputPassword" type="password" placeholder="Введите пароль"/>
	</div>
	<div class="form-group d-flex align-items-center justify-content-between mt-4 mb-0">
        	<a class="small" href="#">Забыли пароль?</a>
            <input class="btn btn-primary" type="submit" value="Авторизоваться">
    </div>
    <div class="form-group d-flex align-items-center justify-content-between mt-4 mb-0">
        <a href="#">
        	<i class="fab fa-google fa-2x" style="color: #d9503e;"></i>
        </a>
        <a href="#">
			<i class="fab fa-vk fa-2x" style="color: #4a658b;"></i>
        </a>
        <a href="#">
        	<i class="fab fa-github fa-2x" style="color: #303030;"></i>
        </a>
        <a href="#">
            <i class="fab fa-facebook fa-2x" style="color: #405794;"></i>
        </a>
    </div>
ss

	if request.method == 'POST':
		form = UserLoginForm(data=request.POST)
		if form.is_valid():
			username = request.POST['user_name']
			password = request.POST['password']
			user  = auth.authenticate(username=username, password=password)
			if user:
				auth.login(request, user)
	else:
'''