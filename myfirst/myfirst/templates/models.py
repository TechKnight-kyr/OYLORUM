from django.db import models
import datetime
from django.utils import timezone

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
exp_models = ['''
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
''']