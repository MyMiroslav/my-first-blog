from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200,blank=True, null=True)
    pretext = models.CharField(max_length=500,blank=True, null=True)
    text = models.TextField()
    telegraph_title = models.ForeignKey('TelegraphArticle',on_delete=models.PROTECT,blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
		
class TelegraphArticle(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title_article = models.CharField(max_length=200,blank=True, null=True)
    url_page_rus = models.CharField(max_length=300,blank=True, null=True)
    url_page_ua = models.CharField(max_length=300,blank=True, null=True)
    url_page_en = models.CharField(max_length=300,blank=True, null=True)