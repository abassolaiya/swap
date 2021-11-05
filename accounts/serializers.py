from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import BusinessProfile

class BusinessSerializer(serializers.ModelSerializer):

    class Meta:
        models = BusinessProfile
        fields = ('business_name', 'business_email', 'number_of_employees',
            'workers')

class UserSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()
    # business = serializers.SerializerMethodField()
    # businessI = serializers.SerializerMethodField()
    # businessD = serializers.SerializerMethodField()
    # business = serializers.SerializerMethodField()


    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name',
            'company')

        def get_company(self, obj):
            qs = obj.company.all()
            return BusinessSerializer(qs).data

class UserCreateSer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validate_data):
        user = User(
            email=validate_data['email'],
            username=validate_data['username'],
            first_name=validate_data['first_name'],
            last_name=validate_data['last_name']
        )
        user.set_password(validate_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
