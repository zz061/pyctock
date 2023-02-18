from django.shortcuts import render

# Create your views here.

from django.http import HttpRequest
from django.http import HttpResponse
def index(request):

    # return HttpResponse('OK!')
    # pass
    text ={'name':'大促商品'}
    return render(request,'book/index.html',context=text)





