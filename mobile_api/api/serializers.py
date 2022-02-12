from .models import Store, Visit
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("pk", "name")
        model = Store


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Visit
