from rest_framework import serializers
from .models import Company, FinancialStatement


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['url', 'name', 'description', 'country', 'industry', 'ceo', 'website', 'image', 'financial_statements']


class FinancialStatementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FinancialStatement
        fields = ['url', 'company', 'date']
