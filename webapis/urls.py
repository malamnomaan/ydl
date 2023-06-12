from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .views import *
from .admin.views import *
from .logging.views import *


urlpatterns = [
    # logging
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('loginweb', loginweb, name='loginweb'),
    path('userlogin', userlogin, name='userlogin'),
    path('userlogout', userlogout, name='userlogout'),
    path('', home, name='home'),
    path('home', home, name='home'),
    path('userprofile', userprofile, name='userprofile'),
    path('myorganization', myorganization, name='myorganization'),

    # admin
    path('getorgdept', getorgdept, name='getorgdept'),
    path('getorg', getorg, name='getorg'),
    path('createupdateorg', createupdateorg, name='createupdateorg'),
    path('createupdatedept', createupdatedept, name='createupdatedept'),
    path('orgainzationsweb', orgainzationsweb, name='orgainzationsweb'),
    path('departmentsweb', departmentsweb, name='departmentsweb'),
    path('usermanagement', usermanagement, name='usermanagement'),
    path('createupdateuser', createupdateuser, name='createupdateuser'),
]


