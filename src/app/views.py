from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import FilterSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    RetrieveDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import EmployeeRecord, DepartmentRecord
from .serializers import EmployeeRecordSerializer, DepartmentRecordSerializer


class EmployeeFilter(FilterSet):
    class Meta:
        model = EmployeeRecord
        fields = {
            "job_title": ["exact"],
            "gender": ["exact"],
            "country": ["exact"],
            "city": ["exact"],
            "department_id": ["exact"],
            "annual_salary": ["gt", "lt"],
        }


class EmployeeList(ListCreateAPIView):
    queryset = EmployeeRecord.objects.all().order_by('employee_id')
    serializer_class = EmployeeRecordSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = EmployeeFilter
    pagination_class = PageNumberPagination
    search_fields = ["^job_title", "^country"]
    ordering_fields = ["annual_salary", "department_id", "bonus", "hire_date"]


class EmployeeDetails(RetrieveUpdateDestroyAPIView):
    queryset = EmployeeRecord.objects.all()
    serializer_class = EmployeeRecordSerializer
    lookup_field = "employee_id"


class DepartmentList(ListCreateAPIView):
    queryset = DepartmentRecord.objects.all()
    serializer_class = DepartmentRecordSerializer


class DepartmentDetails(RetrieveDestroyAPIView):
    queryset = DepartmentRecord.objects.all()
    serializer_class = DepartmentRecordSerializer
    lookup_field = "pk"
