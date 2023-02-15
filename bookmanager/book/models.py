from django.db import models
'''models需要继承 models.Model
    系统会自动添加主键ID
    字段：
    字段名=models。类型
    
'''
class Book(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name


class Peopleinfo(models.Model):
    person = models.CharField(max_length=10)
    gender = models.BooleanField()
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    #id
# Create your models here.
