from rest_framework.routers import DefaultRouter
from api.controllers import UsersController

router = DefaultRouter()

router.register(r"users", UsersController, basename="users")

urlpatterns = router.urls