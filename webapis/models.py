from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from webapis.managers import CustomUserManager

# Create your models here.
class Organization(models.Model):
    org_name = models.CharField(max_length=255)
    org_phone = models.CharField(max_length=255)
    org_email = models.CharField(max_length=255)
    org_contact_person = models.CharField(max_length=255)
    org_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.org_name
    
class Department(models.Model):
    dep_name = models.CharField(max_length=255)
    dep_phone = models.CharField(max_length=255)
    dep_email = models.CharField(max_length=255)
    dep_contact_person = models.CharField(max_length=255)
    dep_description = models.TextField(blank=True, null=True)
    Organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.dep_name

class UserRoles(models.Model):
    role_name = models.CharField(max_length=255)
    role_desc = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    usr_email = models.EmailField(_('email address'), unique=True)
    usr_phone = models.CharField(max_length=12)
    usr_fname = models.CharField(max_length=30, default=None)
    usr_lname = models.CharField(max_length=30, default=None)
    usr_password = models.CharField(max_length=255, default='Admin@1234')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    Organization = models.ForeignKey(Organization,on_delete=models.CASCADE)
    Department = models.ForeignKey(Department,on_delete=models.CASCADE)
    Role = models.ForeignKey(UserRoles,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = 'usr_email'
    REQUIRED_FIELDS = ['usr_phone', 'usr_fname', 'usr_fname']
    objects = CustomUserManager()

    def __str__(self):
        return self.usr_fname + ' ' + self.usr_lname


# CustomUser.objects.create(usr_email='superuser@yardeliver.com', usr_password='admin@1234', usr_phone='9621267608', usr_fname='super', usr_lname='admin',Orgainzation=1,Department_id=1,Role_id=1)