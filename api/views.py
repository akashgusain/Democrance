from rest_framework import viewsets, filters
from .serializers import CustomerSerializer, InsuranceSerializer
from .models import Customer, Insurance


class CustomerViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, editing, filter, searching Customer instances.
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']


class InsuranceViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, editing, filter, searching Insurance instances.
    """
    serializer_class = InsuranceSerializer
    queryset = Insurance.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['type', 'cover', 'premium']
