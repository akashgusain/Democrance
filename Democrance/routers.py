from rest_framework import routers
from api.views import CustomerViewSet, InsuranceViewSet

router = routers.SimpleRouter()

router.register(r'v1/create_customer', CustomerViewSet)
router.register(r'v1/create_policy', InsuranceViewSet)


urlpatterns = router.urls
