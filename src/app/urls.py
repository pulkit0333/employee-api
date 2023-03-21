from django.urls import path
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from .views import EmployeeList , EmployeeDetails , DepartmentList , DepartmentDetails


schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="API for weather data",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('employees/', EmployeeList.as_view(), name='employees-list'),
    path('employees/<str:employee_id>', EmployeeDetails.as_view(), name='employees-details'),
    path('departments/', DepartmentList.as_view(), name='department-list'),
    path('departments/<int:pk>', DepartmentDetails.as_view(), name='department-details'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]