from django.db import models


class UserRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255, default="", blank=True, null=True, unique=True)

    def __str__(self):
        return"{} {}".format(self.role_id, self.role_name)


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255, default="", blank=True, null=True, unique=True)

    def __str__(self):
        return"{} {}".format(self.department_id, self.department_name)


class CollegeUserBasicInfo(models.Model):
    role = models.ForeignKey(UserRole, on_delete=models.PROTECT)
    name = models.CharField(max_length=255, default="", blank=True, null=True)
    email = models.EmailField(max_length=255, primary_key=True, default="")
    password = models.CharField(max_length=255, default="", blank=True, null=True)
    mobile = models.BigIntegerField(default="", null=True, blank=True)
    gender = models.CharField(max_length=255, blank=True, null=True, default="")
    verify_link = models.CharField(max_length=255, default="", blank=True, null=True)
    otp = models.CharField(max_length=255, blank=True, null=True, default="")
    otp_time = models.CharField(max_length=255, blank=True, null=True, default="")
    is_active = models.NullBooleanField(default=0)

    def __str__(self):
        return self.email
