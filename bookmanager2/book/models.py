from django.db import models

class BookInfo(models.Model):
    name = models.CharField(max_length=20,unique=True)
    pub_date = models.DateField(null = True)
    readcount = models.SmallIntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'
        verbose_name = 'book manager'
        pass

class PeopleInfo(models.Model):
    pass

# Create your models here.
