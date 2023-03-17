from rest_framework import serializers
from .models import EmployeeRecord, DepartmentRecord


class EmployeeRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRecord
        fields = '__all__'


class DepartmentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentRecord
        fields = '__all__'
