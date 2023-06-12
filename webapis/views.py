from django.http import response
from django.shortcuts import redirect, render
from django.db.models import Q
from webapis.services.db_service import getallusers
from webapis.models import Department
from webapis.serializer import DepartmentSerializer
from webapis.models import Organization
from webapis.serializer import OrganizationSerializer

from webapis.models import CustomUser 


######################## Routes ###########################

def home(request):
    if request.user.is_authenticated:
        userObj = CustomUser.objects.get(id=request.user.id)
        return render(request,'home.html', {'user':userObj})
    else:
        return redirect('loginweb')

def userprofile(request):
    if request.user.is_authenticated:
        userObj = CustomUser.objects.get(id=request.user.id)
        return render(request,'profile.html', {'user':userObj})
    else:
        return redirect('loginweb')
    
def orgainzationsweb(request):
    if request.user.is_authenticated:
        userObj = CustomUser.objects.filter(id=request.user.id, Role_id=1, Organization_id=1)
        if userObj:
            userObj = userObj[0]
            organizations = Organization.objects.all()
            orgData = OrganizationSerializer(organizations, many=True).data
            return render(request,'organizations.html', {'user':userObj, 'orgs':orgData})
        else:
            return redirect('loginweb')
        
def departmentsweb(request):
    if request.user.is_authenticated:
        userObj = CustomUser.objects.filter(id=request.user.id, Role_id=1, Organization_id=1)
        if userObj:
            userObj = userObj[0]
            departments = Department.objects.all()
            # deptData = DepartmentSerializer(departments, many=True).data
            return render(request,'departments.html', {'user':userObj, 'depts':departments})
        else:
            return redirect('loginweb')
        
def usermanagement(request):
    if request.user.is_authenticated:
        userObj = CustomUser.objects.get(id=request.user.id)
        q = Q()
        if request.user.Role.id != 1:
            q &= Q(Organization_id = request.user.Organization.id)
        allUsers = getallusers(q)
        return render(request,'usermanagement.html', {'user':userObj, 'users':allUsers})
    else:
        return redirect('loginweb')
    
def myorganization(request):
    if request.user.is_authenticated:
        userObj = CustomUser.objects.filter(id=request.user.id, Role_id__in=[1,2])
        if userObj:
            userObj = userObj[0]
            organizations = Organization.objects.filter(id=userObj.Organization.id)
            orgData = OrganizationSerializer(organizations, many=True).data
            return render(request,'myorganization.html', {'user':userObj, 'orgData':orgData})
        else:
            return redirect('loginweb')
        
# APIS
