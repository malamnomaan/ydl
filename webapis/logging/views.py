from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from webapis.models import CustomUser

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['usr_fname'] = f"{user.usr_fname}" 
        token['usr_lname'] = f"{user.usr_lname}" 
        token['usr_organization'] = f"{user.Organization_id}" 
        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

def loginweb(request):
    return render(request, 'login.html')

@csrf_exempt
def userlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user_obj = CustomUser.objects.filter(usr_email = email, is_active=True)
        if user_obj:
            user = authenticate(request, usr_email = email, usr_password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('home')
            else:
                return render(request, 'login.html', {'error':'Invalid Email/Password'})
        else:
            return render(request, 'login.html', {'error':'User Not Found'})
    else:
        return render(request, 'login.html', {'error':''})
    
@csrf_exempt
def userlogout(request):
    logout(request)
    return redirect('loginweb')  # Replace 'home' with the appropriate URL name for your homepage