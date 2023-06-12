from rest_framework import serializers
from webapis.models import Department, Organization

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        exclude = ('is_active','updated_at')

class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = '__all__'