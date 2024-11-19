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

class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    age = models.IntegerField(default=20)
    gender = models.IntegerField(default=1, validators=[validate_gender])
    salary = models.IntegerField(default=-1)
    wealth = models.IntegerField(default=-1)
    tendency = models.IntegerField(default=1, validators=[validate_tendency])

    def __str__(self):
        return self.username
    
from allauth.account.adapter import DefaultAccountAdapter
from django.core.exceptions import ValidationError

class CustomAccountAdapter(DefaultAccountAdapter):
    def clean_gender(self, gender):
        if gender not in [1, 2]:
            raise ValidationError("Gender must be 1 (남성) or 2 (여성).")
        return gender

    def clean_tendency(self, tendency):
        if tendency not in [1, 2, 3, 4, 5]:
            raise ValidationError("Tendency must be between 1 (초고위험) and 5 (초저위험).")
        return tendency

    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)
        data = form.cleaned_data
        user.age = data.get('age', 20)
        user.gender = self.clean_gender(data.get('gender', 1))
        user.salary = data.get('salary', -1)
        user.wealth = data.get('wealth', -1)
        user.tendency = self.clean_tendency(data.get('tendency', 1))
        if commit:
            user.save()
        return user

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