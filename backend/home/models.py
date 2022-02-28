from django.conf import settings
from django.db import models


class Approval(models.Model):
    "Generated Model"
    shape = models.TextField()
    size = models.DecimalField(
        max_digits=3,
        decimal_places=2,
    )
    color = models.TextField()
    clarity = models.TextField()
    rap = models.IntegerField()
    discount = models.SmallIntegerField()
    price = models.BigIntegerField()
    approval = models.TextField()
    date = models.DateTimeField(
        auto_now=True,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="approval_user",
    )
