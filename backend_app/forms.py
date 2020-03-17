from django import forms
from backend_app.models import UserRole, CollegeUserBasicInfo


class UserRoleForm(forms.ModelForm):
    class Meta:
        model = UserRole
        exclude = ['role_id','role_name']


class CollegeUserBasicInfoForms(forms.ModelForm):
    class Meta:
        model = CollegeUserBasicInfo
        exclude = ['role', 'name', 'email','password','gender','mobile','otp','otp_time',
                   'verify_link','is_active']