from rest_framework.routers import DefaultRouter
from api.controllers import UsersController, EditionsController

router = DefaultRouter()

router.register(r"users", UsersController, basename="users")
router.register(r"editions", EditionsController, basename="editions")

urlpatterns = router.urls