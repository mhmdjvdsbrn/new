from rest_framework import routers
from .views import UserView ,PostView

from rest_framework_nested.routers import DefaultRouter


router = DefaultRouter()
router.register('users', UserView, basename='user')
router.register('post', PostView, basename='news')

urlpatterns = router.urls 