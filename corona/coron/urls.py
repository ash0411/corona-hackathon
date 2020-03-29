from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = 'coron'
urlpatters = [
    path('create/',views.article_create,name = 'create'),
]