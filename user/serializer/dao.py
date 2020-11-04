from rest_framework import serializers


class SignupDao(serializers.Serializer):
    firebase_token = serializers.CharField(max_length=255)
