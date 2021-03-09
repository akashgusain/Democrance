from rest_framework import serializers
from .models import Customer, Insurance


class CustomerSerializer(serializers.ModelSerializer):
    """
    used for returning the customer details
    """

    class Meta:
        model = Customer
        fields = '__all__'


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["customer"] = instance.customer.first_name + " "+instance.customer.last_name
        return rep