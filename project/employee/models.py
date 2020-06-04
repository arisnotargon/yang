from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Weather(models.Model):
    name = models.CharField('天気の種類', max_length=20)
    created_at = models.TimeField('日付', default=timezone.now)

    def __str__(self):
        return self.name

class Day(models.Model):
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)
    weather = models.ManyToManyField(Weather, verbose_name='天気(Ctrlで複数選択可)',)
    attach= models.FileField(
        verbose_name = '添付ファイル', 
        upload_to = 'documents/%Y%m/%d/', 
        default='')  #(アスカイ担当)モデル作成

    def __str__(self):
        return self.title, self.attach.url

class Employee(models.Model):
    enterID = models.CharField('EID', max_length=200)
    DTE = models.CharField('DTE', max_length=200)
    
    def __str__(self):
        return self.enterID
        
class Comment(models.Model):
    day = models.ForeignKey('Day', on_delete=models.CASCADE, default="")
    name = models.CharField('名前', max_length=20, blank=True)
    text = models.TextField('コメント内容')
    created_at = models.DateTimeField('日付', default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
