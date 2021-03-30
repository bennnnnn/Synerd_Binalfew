from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    gender = models.CharField(max_length=50, blank=True, null=True)
    street_address = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.CharField(max_length=150, blank=True, null=True)
    phone_number = models.CharField(max_length=150, blank=True, null=True)
    country_of_origin = models.CharField(max_length=150, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    member_organization = models.CharField(max_length=150, blank=True, null=True)




class contactus(models.Model):
    full_name = models.CharField(max_length=80, blank=False, null=False)
    email = models.EmailField(max_length=180, blank=False, null=False)
    subject = models.CharField(max_length=80, blank=False, null=False)
    subject = models.CharField(max_length=80, blank=False, null=False)
    message = models.TextField()
    
    def __str__(self):
        return self.email


class TransferredSubscription(models.Model):
    transfer_from = models.CharField(max_length=50, blank=True, null=True)
    transfer_to = models.CharField(max_length=50, blank=True, null=True)
    request_date = models.DateTimeField(null=True, blank=True)
    transfer_date = models.DateTimeField(null=True, blank=True)



class Subsriber(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    subscriptiontypecode = models.CharField(max_length=50, blank=True, null=True)
    service_code = models.CharField(max_length=50, blank=True, null=True)
    request_date = models.DateTimeField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    service_code = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.username



class Officer(models.Model):
    Subsriber = models.ForeignKey(Subsriber, on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.Subsriber


class Office(models.Model):
    Office = models.ForeignKey(Officer, on_delete=models.CASCADE)
    office_name = models.CharField(max_length=50, blank=True, null=True)
    attribution = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.Office




class OrganizationMember(models.Model):
    subscriber = models.ForeignKey(Subsriber, on_delete=models.CASCADE)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    country = models.CharField(max_length=150, blank=True, null=True)
    citizenship = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.subscriber


class Organization(models.Model):
    organization_name = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField()
    date_joined = models.DateTimeField(null=True, blank=True)
    address1 = models.CharField(max_length=150, blank=True, null=True)
    address2 = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    zipcode = models.CharField(max_length=150, blank=True, null=True)
    phone_number = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.organization_name