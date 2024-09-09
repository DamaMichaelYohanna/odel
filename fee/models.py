from django.db import models


class SchoolFee(models.Model):
    """database model for school fee."""
    amount = models.IntegerField()
    year = models.IntegerField()
    for_indigene = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.amount}"


class AcceptanceFee(models.Model):
    """database model for acceptance fee."""
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.amount}"
