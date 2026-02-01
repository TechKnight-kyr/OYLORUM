from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'articles'

urlpatterns = [
    path('profile/', views.my_profile, name='profile'),
    path('profile/delete/<int:article_id>/', views.delete_article, name='delete_article'),
    path('', views.begin, name='begin'),
    path('page1/', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('leave_artc/', views.leave_artc, name='leave_artc'),

    path('login/', views.login, name='login'),
    path('reg/', views.registration, name='registration'),

    path('logout/', LogoutView.as_view(), name='logout'),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# Это должно быть ВНЕ списка urlpatterns, в самом конце файла
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)