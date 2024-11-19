from rest_framework import serializers
from .models import User
from django.core.exceptions import ValidationError
from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(default=20)
    gender = serializers.IntegerField(default=1)
    salary = serializers.IntegerField(default=-1)
    wealth = serializers.IntegerField(default=-1)
    tendency = serializers.IntegerField(default=1)

    class Meta:
        model = User
        fields = ['username', 'password', 'age', 'gender', 'salary', 'wealth', 'tendency']

    def validate_gender(self, value):
        if value not in [1, 2]:
            raise serializers.ValidationError("Gender must be 1 (남성) or 2 (여성).")
        return value

    def validate_tendency(self, value):
        if value not in [1, 2, 3, 4, 5]:
            raise serializers.ValidationError("Tendency must be between 1 (초고위험) and 5 (초저위험).")
        return value

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['age'] = self.validated_data.get('age', 20)
        data['gender'] = self.validated_data.get('gender', 1)
        data['salary'] = self.validated_data.get('salary', -1)
        data['wealth'] = self.validated_data.get('wealth', -1)
        data['tendency'] = self.validated_data.get('tendency', 1)
        return data

    def save(self, request):
        user = super().save(request)
        user.age = self.validated_data.get('age', 20)
        user.gender = self.validated_data.get('gender', 1)
        user.salary = self.validated_data.get('salary', -1)
        user.wealth = self.validated_data.get('wealth', -1)
        user.tendency = self.validated_data.get('tendency', 1)
        user.save()
        return user


from dj_rest_auth.serializers import UserDetailsSerializer

class CustomUserDetailsSerializer(UserDetailsSerializer):
    age = serializers.IntegerField(read_only=False, required=False)
    gender = serializers.IntegerField(read_only=False, required=False)
    salary = serializers.IntegerField(read_only=False, required=False)
    wealth = serializers.IntegerField(read_only=False, required=False)
    tendency = serializers.IntegerField(read_only=False, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'age', 'gender', 'salary', 'wealth', 'tendency']
        read_only_fields = ['id', 'username']

    def validate_gender(self, value):
        if value not in [1, 2]:
            raise serializers.ValidationError("Gender must be 1 (남성) or 2 (여성).")
        return value

    def validate_tendency(self, value):
        if value not in [1, 2, 3, 4, 5]:
            raise serializers.ValidationError("Tendency must be between 1 (초고위험) and 5 (초저위험).")
        return value
