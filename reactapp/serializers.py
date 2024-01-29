from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.models import Project
from .models import GetQuote, ContactUs


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

class GetAQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetQuote
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'confirm_password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')

        # Perform password validation here
        if password != confirm_password:
            raise serializers.ValidationError("Passwords don't match")

        user = get_user_model().objects.create_user(**validated_data)
        user.set_password(password)  # Set the password before saving the user
        user.save()
        return user