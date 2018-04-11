from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^new_telegraph_article_form', views.new_telegraph_article_form, name='new_telegraph_article_form'),
    url(r'^add_and_parse_new_telegraph_article', views.add_and_parse_new_telegraph_article, name='add_and_parse_new_telegraph_article'),
]