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
    enterID = models.CharField('EID/名前', max_length=200)
    DTE = models.CharField('所属DTE', max_length=200)
    homeoffice = models.CharField('ホームオフィス', max_length=200)
    email = models.CharField('メールアドレス', max_length=200)
    number = models.CharField('社員番号', max_length=200)
    family_name = models.CharField('姓', max_length=200)
    last_name = models.CharField('名', max_length=200)
    role = models.CharField('ロール', max_length=200)
    career_level = models.CharField('キャリアレベル', max_length=200)
    team = models.CharField('所属チーム', max_length=200)
    
    def __str__(self):
        return self.enterID
        
class Comment(models.Model):
    day = models.ForeignKey('Day', on_delete=models.CASCADE, default="")
    name = models.CharField('名前', max_length=20, blank=True)
    text = models.TextField('コメント内容')
    created_at = models.DateTimeField('日付', default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
