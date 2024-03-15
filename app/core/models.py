from django.db import models
from django.db.models.functions import Lower


class Artist(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("name"),
                name="unique_name",
            ),
        ]
