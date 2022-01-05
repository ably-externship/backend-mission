from django.db import models


class Customer(models.Model):
    user_id = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    name = models.CharField(max_length=5)
    birth = models.DateField()
    sex = models.IntegerField()
    phone = models.IntegerField()
    email = models.CharField(max_length=60)
    address = models.IntegerField()
    maritial_status = models.IntegerField(blank=True, null=None)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer'


class Employee(models.Model):
    employee_id = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    name = models.CharField(max_length=5)
    birth = models.DateField()
    sex = models.IntegerField()
    phone = models.IntegerField()
    email = models.CharField(max_length=60)
    address = models.IntegerField()
    department_id = models.IntegerField()
    salary = models.IntegerField()
    job_id = models.IntegerField()
    hire_date = models.DateField()
    maritial_status = models.IntegerField(blank=True, null=None)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'employee'
