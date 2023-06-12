from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from webapis.models import CustomUser
from webapis.services.db_service import create_update_dept, create_update_org, get_org, get_org_dept
from webapis.managers import CustomUserManager


@csrf_exempt
@api_view(['get'])
def getorgdept(request):
    '''
        API to fetch all the department in organization
    '''
    org_id = request.data.get('org_id')
    q = Q()
    q &= Q(is_active=True)
    if org_id:
        q &= Q(Organization_id = org_id)
    data = get_org_dept(q)
    if data:
        return Response({
            'status':True,
            'statuscode':200,
            'data':data},
            status=HTTP_200_OK)
    else:
        return Response({
            'status':False,
            'statuscode':400,
            'data':[]},
            status=HTTP_400_BAD_REQUEST)
    
@csrf_exempt
@api_view(['get'])
def getorg(request):
    '''
        API to fetch all the organization
    '''
    q = Q()
    q &= Q(is_active=True)
    data = get_org(q)
    if data:
        return Response({
            'status':True,
            'statuscode':200,
            'data':data},
            status=HTTP_200_OK)
    else:
        return Response({
            'status':False,
            'statuscode':400,
            'data':[]},
            status=HTTP_400_BAD_REQUEST)
    
@csrf_exempt
@api_view(['post'])
def createupdateorg(request):
    '''
        API to create/update orgainzation
    '''
    org_name = request.data.get('org_name')
    org_phone = request.data.get('org_phone')
    org_email = request.data.get('org_email')
    org_contact_person = request.data.get('org_contact_person')
    org_description = request.data.get('org_description')
    org_id = request.data.get('org_id')

    if not org_id:
        org_id = 0

    error_list = []
    if not org_name:
        error_list.append({'org_name' : 'org_name cannot be null'})
    if not org_phone:
        error_list.append({'org_phone' : 'org_phone cannot be null'})
    if not org_email:
        error_list.append({'org_email' : 'org_email cannot be null'})
    if not org_contact_person:
        error_list.append({'org_contact_person' : 'org_contact_person cannot be null'})
    if len(error_list):
        return Response({
            'status':True,
            'statuscode':200,
            'message':'error in payload json',
            'error' : error_list
            },
            status=HTTP_200_OK)

    message, success = create_update_org(org_name,org_phone,org_email,org_contact_person,org_description,org_id)

    if success:
        return Response({
            'status':True,
            'statuscode':200,
            'message':message,
            'error' : error_list
            },
            status=HTTP_200_OK)
    else:
        return Response({
            'status':False,
            'statuscode':400,
            'message':message,
            'error' : error_list
            },
            status=HTTP_200_OK)
    
@csrf_exempt
@api_view(['post'])
def createupdatedept(request):
    '''
        API to fetch all the dept
    '''
    dept_name = request.data.get('dept_name')
    dept_phone = request.data.get('dept_phone')
    dept_email = request.data.get('dept_email')
    dept_contact_person = request.data.get('dept_contact_person')
    dept_description = request.data.get('dept_description')
    dept_id = request.data.get('dept_id')
    org_id = request.data.get('org_id')

    if not dept_id:
        dept_id = 0

    error_list = []
    if not dept_name:
        error_list.append({'dept_name' : 'dept_name cannot be null'})
    if not dept_phone:
        error_list.append({'dept_phone' : 'dept_phone cannot be null'})
    if not dept_email:
        error_list.append({'dept_email' : 'dept_email cannot be null'})
    if not dept_contact_person:
        error_list.append({'dept_contact_person' : 'dept_contact_person cannot be null'})
    if not org_id:
        error_list.append({'org_id' : 'org_id cannot be null'})
    if len(error_list):
        return Response({
            'status':True,
            'statuscode':200,
            'message':'error in payload json',
            'error' : error_list
            },
            status=HTTP_200_OK)

    message, success = create_update_dept(dept_name,dept_phone,dept_email,dept_contact_person,dept_description,dept_id, org_id)

    if success:
        return Response({
            'status':True,
            'statuscode':200,
            'message':message,
            'error' : error_list
            },
            status=HTTP_200_OK)
    else:
        return Response({
            'status':False,
            'statuscode':400,
            'message':message,
            'error' : error_list
            },
            status=HTTP_200_OK)

@csrf_exempt
@api_view(['post'])
def createupdateuser(request):
    '''
        API to Create New User
    '''
    
    usr_id = request.data.get('usr_id')
    usr_fname = request.data.get('usr_fname')
    usr_lname = request.data.get('usr_lname')
    usr_phone = request.data.get('usr_phone')
    usr_email = request.data.get('usr_email')
    usr_password = request.data.get('usr_password')
    usr_org = request.data.get('usr_org')
    usr_dept = request.data.get('usr_dept')
    usr_role = request.data.get('usr_role')

    error_list = []
    if not usr_fname:
        error_list.append({'usr_fname' : 'usr_fname cannot be null'})
    if not usr_lname:
        error_list.append({'usr_lname' : 'usr_lname cannot be null'})
    if not usr_phone:
        error_list.append({'usr_phone' : 'usr_phone cannot be null'})
    if not usr_email:
        error_list.append({'usr_email' : 'usr_email cannot be null'})
    if not usr_password:
        error_list.append({'usr_password' : 'usr_password cannot be null'})
    if not usr_org:
        error_list.append({'usr_org' : 'usr_org cannot be null'})
    if not usr_dept:
        error_list.append({'usr_dept' : 'usr_dept cannot be null'})
    if not usr_role:
        error_list.append({'usr_role' : 'usr_role cannot be null'})

    if len(error_list):
        return Response({
            'status':False,
            'statuscode':400,
            'message':'error in payload json',
            'error' : error_list
            },
            status=HTTP_200_OK)
    
    if usr_id:
        try:
            userobj = CustomUser.objects.get(id=usr_id)
        except CustomUser.DoesNotExist:
            return Response({
                'status': False,
                'statuscode': 400,
                'message': f'User with id {usr_id} not found',
                'error': error_list
            }, status=HTTP_200_OK)
        if userobj:
            
            userobj.usr_email=usr_email
            userobj.usr_phone=usr_phone
            userobj.usr_fname=usr_fname
            userobj.usr_lname=usr_lname
            userobj.is_staff=True
            userobj.Organization_id=int(usr_org)
            userobj.Department_id=int(usr_dept)
            userobj.Role_id=int(usr_role)
            userobj.save()
            
            message = "User Updated Successfully"
        else:
            return Response({
            'status':False,
            'statuscode':400,
            'message':'User with id {usr_id} not found',
            'error' : error_list
            },
            status=HTTP_200_OK)
    else:
        userobj = CustomUser.objects.create(
            usr_email=usr_email,
            usr_phone=usr_phone,
            usr_fname=usr_fname,
            usr_lname=usr_lname,
            is_staff=True,
            Organization_id=int(usr_org),
            Department_id=int(usr_dept),
            Role_id=int(usr_role)
            )
        message = "User Created Successfully"
    print(userobj)
    userobj.set_password(usr_password)
    userobj.save()

    return Response({
            'status':True,
            'statuscode':200,
            'message':message,
            'error' : error_list
            },
            status=HTTP_200_OK)
    