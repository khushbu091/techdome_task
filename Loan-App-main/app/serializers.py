from rest_framework import serializers
from . import models

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Loan
        fields = ['id', 'customer', 'amount', 'term', 'state']

class RepaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Repayment
        fields = ['id', 'loan', 'amount', 'date', 'status']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'
