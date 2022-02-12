from django.db import models
from django.core.validators import RegexValidator


class Employer(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name="Employer name",
        help_text="Employer name",
    )
    phone_regex = RegexValidator(
        regex=r"^(7)?[0-9]{10}$",  # "/^([7]?[0-9]{3,11})*$/i;",
        message="Phone number should be like 7XXXXXXXXXX (X-num from 0 to 9)",
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=11, blank=False
    )

    class Meta:
        verbose_name = "Employer"
        verbose_name_plural = "Employers"

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name="Store",
        help_text="Store",
    )
    employer = models.ForeignKey(
        Employer,
        on_delete=models.CASCADE,
        related_name="store",
        null=False,
        verbose_name="Employer",
        help_text="Employer",
    )

    class Meta:
        verbose_name = "Store"
        verbose_name_plural = "Stores"

    def __str__(self):
        return str(self.pk)


class Visit(models.Model):
    date = models.DateTimeField(
        "Date", auto_now_add=True, db_index=True, help_text="Visit date"
    )
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name="visit",
        null=False,
        verbose_name="Store",
        help_text="Store",
    )
    lon = models.FloatField()
    lat = models.FloatField()

    class Meta:
        verbose_name = "Visit"
        verbose_name_plural = "Visits"

    def __str__(self):
        return str(self.store)
