from django.db import models

class Tag(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    tags = models.TextField()  # This will store the comma-separated tags

    def __str__(self):
        return self.sku
