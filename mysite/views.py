from django.http import HttpResponse
import datetime

def index(request):
    return HttpResponse("hello, world. you're at kevin's page.")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body> it's now %s. </body></html>" % now 
    return HttpResponse(html)

def hello(request):
    return HttpResponse("Hello World")

def hello1(request):
    return HttpResponse("this is hello1")
