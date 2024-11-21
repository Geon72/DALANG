from rest_framework import serializers
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer


class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(default=20)
    gender = serializers.IntegerField(default=1)
    salary = serializers.IntegerField(default=-1)
    wealth = serializers.IntegerField(default=-1)
    tendency = serializers.IntegerField(default=1)
    marital_status = serializers.IntegerField(default=0)
    num_of_dependents = serializers.IntegerField(default=0)
    employment_status = serializers.IntegerField(default=0)
    credit_score = serializers.IntegerField(default=0)
    monthly_expense = serializers.IntegerField(default=0)
    investment_experience = serializers.IntegerField(default=0)

    class Meta:
        model = User
        fields = [
            'username', 'password', 'age', 'gender', 'salary', 'wealth', 
            'tendency', 'marital_status', 'num_of_dependents', 
            'employment_status', 'credit_score', 'monthly_expense', 
            'investment_experience'
        ]

    def validate_gender(self, value):
        if value not in [1, 2]:
            raise serializers.ValidationError("Gender must be 1 (남성) or 2 (여성).")
        return value

    def validate_tendency(self, value):
        if value not in [1, 2, 3, 4, 5]:
            raise serializers.ValidationError("Tendency must be between 1 (초고위험) and 5 (초저위험).")
        return value

    def validate_marital_status(self, value):
        if value not in [0, 1]:
            raise serializers.ValidationError("Marital status must be 0 (미혼) or 1 (기혼).")
        return value

    def validate_employment_status(self, value):
        if value not in [0, 1]:
            raise serializers.ValidationError("Employment status must be 0 (실업) or 1 (고용).")
        return value

    def validate_investment_experience(self, value):
        if value not in [0, 1]:
            raise serializers.ValidationError("Investment experience must be 0 (없음) or 1 (있음).")
        return value

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data.update({
            'age': self.validated_data.get('age', 20),
            'gender': self.validated_data.get('gender', 1),
            'salary': self.validated_data.get('salary', -1),
            'wealth': self.validated_data.get('wealth', -1),
            'tendency': self.validated_data.get('tendency', 1),
            'marital_status': self.validated_data.get('marital_status', 0),
            'num_of_dependents': self.validated_data.get('num_of_dependents', 0),
            'employment_status': self.validated_data.get('employment_status', 0),
            'credit_score': self.validated_data.get('credit_score', 0),
            'monthly_expense': self.validated_data.get('monthly_expense', 0),
            'investment_experience': self.validated_data.get('investment_experience', 0),
        })
        return data

    def save(self, request):
        user = super().save(request)
        user.age = self.validated_data.get('age', 20)
        user.gender = self.validated_data.get('gender', 1)
        user.salary = self.validated_data.get('salary', -1)
        user.wealth = self.validated_data.get('wealth', -1)
        user.tendency = self.validated_data.get('tendency', 1)
        user.marital_status = self.validated_data.get('marital_status', 0)
        user.num_of_dependents = self.validated_data.get('num_of_dependents', 0)
        user.employment_status = self.validated_data.get('employment_status', 0)
        user.credit_score = self.validated_data.get('credit_score', 0)
        user.monthly_expense = self.validated_data.get('monthly_expense', 0)
        user.investment_experience = self.validated_data.get('investment_experience', 0)
        user.save()
        return user


class CustomUserDetailsSerializer(UserDetailsSerializer):
    age = serializers.IntegerField(read_only=False, required=False)
    gender = serializers.IntegerField(read_only=False, required=False)
    salary = serializers.IntegerField(read_only=False, required=False)
    wealth = serializers.IntegerField(read_only=False, required=False)
    tendency = serializers.IntegerField(read_only=False, required=False)
    marital_status = serializers.IntegerField(read_only=False, required=False)
    num_of_dependents = serializers.IntegerField(read_only=False, required=False)
    employment_status = serializers.IntegerField(read_only=False, required=False)
    credit_score = serializers.IntegerField(read_only=False, required=False)
    monthly_expense = serializers.IntegerField(read_only=False, required=False)
    investment_experience = serializers.IntegerField(read_only=False, required=False)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'age', 'gender', 'salary', 'wealth', 'tendency', 
            'marital_status', 'num_of_dependents', 'employment_status', 
            'credit_score', 'monthly_expense', 'investment_experience'
        ]
        read_only_fields = ['id', 'username']

    def validate_gender(self, value):
        if value not in [1, 2]:
            raise serializers.ValidationError("Gender must be 1 (남성) or 2 (여성).")
        return value

    def validate_tendency(self, value):
        if value not in [1, 2, 3, 4, 5]:
            raise serializers.ValidationError("Tendency must be between 1 (초고위험) and 5 (초저위험).")
        return value

    def validate_marital_status(self, value):
        if value not in [0, 1]:
            raise serializers.ValidationError("Marital status must be 0 (미혼) or 1 (기혼).")
        return value

    def validate_employment_status(self, value):
        if value not in [0, 1]:
            raise serializers.ValidationError("Employment status must be 0 (실업) or 1 (고용).")
        return value

    def validate_investment_experience(self, value):
        if value not in [0, 1]:
            raise serializers.ValidationError("Investment experience must be 0 (없음) or 1 (있음).")
        return value


# from rest_framework import serializers
# from .models import User
# from django.core.exceptions import ValidationError
# from dj_rest_auth.registration.serializers import RegisterSerializer

# class CustomRegisterSerializer(RegisterSerializer):
#     age = serializers.IntegerField(default=20)
#     gender = serializers.IntegerField(default=1)
#     salary = serializers.IntegerField(default=-1)
#     wealth = serializers.IntegerField(default=-1)
#     tendency = serializers.IntegerField(default=1)

#     class Meta:
#         model = User
#         fields = ['username', 'password', 'age', 'gender', 'salary', 'wealth', 'tendency']

#     def validate_gender(self, value):
#         if value not in [1, 2]:
#             raise serializers.ValidationError("Gender must be 1 (남성) or 2 (여성).")
#         return value

#     def validate_tendency(self, value):
#         if value not in [1, 2, 3, 4, 5]:
#             raise serializers.ValidationError("Tendency must be between 1 (초고위험) and 5 (초저위험).")
#         return value

#     def get_cleaned_data(self):
#         data = super().get_cleaned_data()
#         data['age'] = self.validated_data.get('age', 20)
#         data['gender'] = self.validated_data.get('gender', 1)
#         data['salary'] = self.validated_data.get('salary', -1)
#         data['wealth'] = self.validated_data.get('wealth', -1)
#         data['tendency'] = self.validated_data.get('tendency', 1)
#         return data

#     def save(self, request):
#         user = super().save(request)
#         user.age = self.validated_data.get('age', 20)
#         user.gender = self.validated_data.get('gender', 1)
#         user.salary = self.validated_data.get('salary', -1)
#         user.wealth = self.validated_data.get('wealth', -1)
#         user.tendency = self.validated_data.get('tendency', 1)
#         user.save()
#         return user


# from dj_rest_auth.serializers import UserDetailsSerializer

# class CustomUserDetailsSerializer(UserDetailsSerializer):
#     age = serializers.IntegerField(read_only=False, required=False)
#     gender = serializers.IntegerField(read_only=False, required=False)
#     salary = serializers.IntegerField(read_only=False, required=False)
#     wealth = serializers.IntegerField(read_only=False, required=False)
#     tendency = serializers.IntegerField(read_only=False, required=False)

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'age', 'gender', 'salary', 'wealth', 'tendency']
#         read_only_fields = ['id', 'username']

#     def validate_gender(self, value):
#         if value not in [1, 2]:
#             raise serializers.ValidationError("Gender must be 1 (남성) or 2 (여성).")
#         return value

#     def validate_tendency(self, value):
#         if value not in [1, 2, 3, 4, 5]:
#             raise serializers.ValidationError("Tendency must be between 1 (초고위험) and 5 (초저위험).")
#         return value
