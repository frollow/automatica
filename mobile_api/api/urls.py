from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, StoreViewSet, VisitViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(
    r"(?P<phone_number>\d+)/stores",
    StoreViewSet,
    basename="stores",
)
router.register(
    r"(?P<phone_number>\d+)/visits",
    VisitViewSet,
    basename="visits",
)


urlpatterns = [
    path("v1/", include(router.urls)),
    path(
        "api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
]
