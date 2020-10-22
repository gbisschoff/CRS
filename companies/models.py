from django.db import models
from django_countries.fields import CountryField
from .industry import INDUSTRY_CHOICES


class Company(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    country = CountryField()
    industry = models.CharField(choices=INDUSTRY_CHOICES, max_length=6)
    ceo = models.CharField(max_length=100, blank=True, default='')
    website = models.URLField(max_length=100)
    image = models.ImageField(upload_to='companies')

    def __str__(self):
        return self.name


class FinancialStatement(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='financial_statements')
    date = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['company', 'date'], name='unique_company_financial_statement')
        ]

    def __str__(self):
        return str(self.date)
