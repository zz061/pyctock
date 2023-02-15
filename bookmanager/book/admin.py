from django.contrib import admin

# Register your models here.
from book.models import Book,Peopleinfo
admin.site.register(Book)
admin.site.register(Peopleinfo)

