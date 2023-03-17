from django.db import models

class DepartmentRecord(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class EmployeeRecord(models.Model):
    employee_id = models.CharField(max_length=22, primary_key=True)
    full_name = models.CharField(max_length=60)
    job_title = models.CharField(max_length=255)
    department = models.ForeignKey(DepartmentRecord, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    hire_date = models.DateField()
    annual_salary = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    bonus = models.CharField(max_length=5)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    exit_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.employee_id} ({self.full_name})"
