from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH

# Create your models here.


class User(AbstractUser):

    """User Model"""

    Gender_Male = "male"
    Gender_Female = "female"
    Gender_Other = "other"

    Gender_Choice = (
        (Gender_Male, "male"),
        (Gender_Female, "female"),
        (Gender_Other, "other"),
    )

    Language_English = "en"
    Language_Korean = "kr"

    Language_Choice = (
        (Language_English, "en"),
        (Language_Korean, "kr"),
    )

    currency_USD = "usd"
    currency_KRW = "krw"

    currency_Choice = (
        (currency_USD, "usd"),
        (currency_KRW, "krw"),
    )

    Avatar = models.ImageField(blank=True)
    Gender = models.CharField(choices=Gender_Choice, max_length=10, blank=True)
    Bio = models.TextField(blank=True)
    Birthdate = models.DateField(null=True)
    Language = models.TextField(
        choices=Language_Choice, max_length=2, blank=True)
    currency = models.TextField(
        choices=currency_Choice, max_length=3, blank=True)
    Superhost = models.BooleanField(default=False)
