from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Custom validation functions
def validate_gender(value):
    if value not in [1, 2]:
        raise ValidationError("Gender must be 1 (남성) or 2 (여성).")

def validate_tendency(value):
    if value not in [1, 2, 3, 4, 5]:
        raise ValidationError("Tendency must be between 1 (초고위험) and 5 (초저위험).")

def validate_marital_status(value):
    if value not in [0, 1]:
        raise ValidationError("Marital status must be 0 (미혼) or 1 (기혼).")

def validate_employment_status(value):
    if value not in [0, 1]:
        raise ValidationError("Employment status must be 0 (실업) or 1 (고용).")

def validate_investment_experience(value):
    if value not in [0, 1]:
        raise ValidationError("Investment experience must be 0 (없음) or 1 (있음).")

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    age = models.IntegerField(default=20)
    gender = models.IntegerField(default=1, validators=[validate_gender])
    salary = models.IntegerField(default=-1)
    wealth = models.IntegerField(default=-1)
    tendency = models.IntegerField(default=1, validators=[validate_tendency])
    marital_status = models.IntegerField(default=0, validators=[validate_marital_status])  # 0: 미혼, 1: 기혼
    num_of_dependents = models.IntegerField(default=0)  # 부양가족 수
    employment_status = models.IntegerField(default=0, validators=[validate_employment_status])  # 0: 실업, 1: 고용
    credit_score = models.IntegerField(default=0)  # 신용 점수
    monthly_expense = models.IntegerField(default=0)  # 월평균 지출
    investment_experience = models.IntegerField(default=0, validators=[validate_investment_experience])  # 0: 없음, 1: 있음

    def __str__(self):
        return self.username



from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def clean_gender(self, gender):
        if gender not in [1, 2]:
            raise ValidationError("Gender must be 1 (남성) or 2 (여성).")
        return gender

    def clean_tendency(self, tendency):
        if tendency not in [1, 2, 3, 4, 5]:
            raise ValidationError("Tendency must be between 1 (초고위험) and 5 (초저위험).")
        return tendency

    def clean_marital_status(self, marital_status):
        if marital_status not in [0, 1]:
            raise ValidationError("Marital status must be 0 (미혼) or 1 (기혼).")
        return marital_status

    def clean_employment_status(self, employment_status):
        if employment_status not in [0, 1]:
            raise ValidationError("Employment status must be 0 (실업) or 1 (고용).")
        return employment_status

    def clean_investment_experience(self, investment_experience):
        if investment_experience not in [0, 1]:
            raise ValidationError("Investment experience must be 0 (없음) or 1 (있음).")
        return investment_experience

    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)
        data = form.cleaned_data
        user.age = data.get('age', 20)
        user.gender = self.clean_gender(data.get('gender', 1))
        user.salary = data.get('salary', -1)
        user.wealth = data.get('wealth', -1)
        user.tendency = self.clean_tendency(data.get('tendency', 1))
        user.marital_status = self.clean_marital_status(data.get('marital_status', 0))
        user.num_of_dependents = data.get('num_of_dependents', 0)
        user.employment_status = self.clean_employment_status(data.get('employment_status', 0))
        user.credit_score = data.get('credit_score', 0)
        user.monthly_expense = data.get('monthly_expense', 0)
        user.investment_experience = self.clean_investment_experience(data.get('investment_experience', 0))
        if commit:
            user.save()
        return user


# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.core.exceptions import ValidationError

# # Custom validation functions
# def validate_gender(value):
#     if value not in [1, 2]:
#         raise ValidationError("Gender must be 1 (남성) or 2 (여성).")

# def validate_tendency(value):
#     if value not in [1, 2, 3, 4, 5]:
#         raise ValidationError("Tendency must be between 1 (초고위험) and 5 (초저위험).")
# class User(AbstractUser):
#     username = models.CharField(max_length=20, unique=True)
#     age = models.IntegerField(default=20)
#     gender = models.IntegerField(default=1, validators=[validate_gender])
#     salary = models.IntegerField(default=-1)
#     wealth = models.IntegerField(default=-1)
#     tendency = models.IntegerField(default=1, validators=[validate_tendency])

#     def __str__(self):
#         return self.username
    
# from allauth.account.adapter import DefaultAccountAdapter
# from django.core.exceptions import ValidationError

# class CustomAccountAdapter(DefaultAccountAdapter):
#     def clean_gender(self, gender):
#         if gender not in [1, 2]:
#             raise ValidationError("Gender must be 1 (남성) or 2 (여성).")
#         return gender

#     def clean_tendency(self, tendency):
#         if tendency not in [1, 2, 3, 4, 5]:
#             raise ValidationError("Tendency must be between 1 (초고위험) and 5 (초저위험).")
#         return tendency

#     def save_user(self, request, user, form, commit=True):
#         user = super().save_user(request, user, form, commit=False)
#         data = form.cleaned_data
#         user.age = data.get('age', 20)
#         user.gender = self.clean_gender(data.get('gender', 1))
#         user.salary = data.get('salary', -1)
#         user.wealth = data.get('wealth', -1)
#         user.tendency = self.clean_tendency(data.get('tendency', 1))
#         if commit:
#             user.save()
#         return user

# # Create your models here.
# class User(AbstractUser):
#   nickname = models.CharField(max_length=100)

# from allauth.account.adapter import DefaultAccountAdapter

# class CustomAccountAdapter(DefaultAccountAdapter):
#   def save_user(self, request, user, form, commit=True):
#     """
#     Saves a new `User` instance using information provided in the
#     signup form.
#     """
#     from allauth.account.utils import user_email, user_field, user_username
#     data = form.cleaned_data
#     first_name = data.get("first_name")
#     last_name = data.get("last_name")
#     email = data.get("email")
#     username = data.get("username")
#     # nickname 필드를 추가
#     nickname = data.get("nickname")
#     user_email(user, email)
#     user_username(user, username)
#     if first_name:
#       user_field(user, "first_name", first_name)
#     if last_name:
#       user_field(user, "last_name", last_name)
#     if nickname:
#       user_field(user, "nickname", nickname)
#     if "password1" in data:
#       user.set_password(data["password1"])
#     else:
#       user.set_unusable_password()
#     self.populate_username(request, user)
#     if commit:
#       # Ability not to commit makes it easier to derive from
#       # this adapter by adding
#       user.save()
#     return user