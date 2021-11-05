from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BusinessProfile(models.Model):
    workers = models.ManyToManyField(User, related_name='company')
    business_name = models.CharField(max_length=200)
    number_of_employees = models.IntegerField(blank=True, null=True)
    business_email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business_name
