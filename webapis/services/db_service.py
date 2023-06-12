from webapis.models import Department, Organization, CustomUser

from webapis.serializer import DepartmentSerializer,OrganizationSerializer

def get_org_dept(q):
    queryset = Department.objects.filter(q).order_by('Organization_id','created_at')
    parseddata = DepartmentSerializer(queryset,many=True).data
    return parseddata

def get_org(q):
    queryset = Organization.objects.filter(q).order_by('id','created_at')
    parseddata = OrganizationSerializer(queryset,many=True).data
    return parseddata

def create_update_org(org_name,org_phone,org_email,org_contact_person,org_description, org_id):
    if org_id:
        org_obj = Organization.objects.filter(id=org_id)
        if org_obj:
            org_obj.update(org_name=org_name, org_phone=org_phone, org_email=org_email, org_contact_person=org_contact_person, org_description=org_description)
            return 'Orgainzation updated successfully', True
        else:
            return 'Orgainzation not exist', False
    else:
        Organization.objects.create(org_name=org_name, org_phone=org_phone, org_email=org_email, org_contact_person=org_contact_person, org_description=org_description)
        message = 'Orgainzation Created successfully'
        return message, True
    
def create_update_dept(dept_name,dept_phone,dept_email,dept_contact_person,dept_description,dept_id,org_id):
    if dept_id:
        dept_obj = Department.objects.filter(id=dept_id)
        print(dept_obj)
        if dept_obj:
            dept_obj.update(dep_name=dept_name, dep_phone=dept_phone, dep_email=dept_email, dep_contact_person=dept_contact_person, dep_description=dept_description,Organization_id=org_id)
            return 'Department updated sucessfully', True
        else:
            return 'Department not exist', False
    else:
        Department.objects.create(dept_name=dept_name, dept_phone=dept_phone, dept_email=dept_email, dept_contact_person=dept_contact_person, org_description=dept_description)
        message = 'Department Created successfully'
        return message, True
    
def getallusers(q):
    usr_obj = CustomUser.objects.filter(q)
    return usr_obj