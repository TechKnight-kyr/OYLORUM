from django.apps import AppConfig


class ArticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'articles'
    verbose_name = 'Блог'

ap_ex = ['''verbose_ name = 'something - это метод чтобы задать название отдела''']