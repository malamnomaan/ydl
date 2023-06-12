from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Hi Welcome to api server')
