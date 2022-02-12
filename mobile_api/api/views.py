from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Store, Visit
from rest_framework import viewsets
from .serializers import UserSerializer, StoreSerializer, VisitSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StoreViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StoreSerializer

    def get_queryset(self):
        store = Store.objects.filter(
            employer__phone_number=self.kwargs.get("phone_number")
        )
        return store


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

    def perform_create(self, serializer):
        queryset = Store.objects.filter(
            employer__phone_number=self.kwargs.get("phone_number")
        ).filter(pk=str(serializer.validated_data["store"]))
        if not queryset.exists():
            raise ValidationError(
                "The employee's phone number is not linked to this store"
            )
        serializer.save()
