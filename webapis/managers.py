from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _



class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, usr_email, usr_password, usr_phone, usr_fname, usr_lname, usr_org, usr_dept, usr_role, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not usr_email:
            raise ValueError(_('The User Email must be set'))
        if not usr_phone:
            raise ValueError(_('The User Phone Number must be set'))
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)

        usr_email = self.normalize_email(usr_email)
        user = self.model(usr_email=usr_email, usr_phone=usr_phone, usr_fname=usr_fname, usr_lname=usr_lname, Organization_id=usr_org, Department_id=usr_dept, Role_id = usr_role,**extra_fields)
        user.set_password(usr_password)
        user.save()
        return user

    def create_superuser(self, usr_email, usr_password, usr_phone, usr_fname, usr_lname, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('Organization_id', 1)
        extra_fields.setdefault('Department_id', 1)
        extra_fields.setdefault('Role_id', 1)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(usr_email, usr_password, usr_phone, usr_fname, usr_lname, **extra_fields)
