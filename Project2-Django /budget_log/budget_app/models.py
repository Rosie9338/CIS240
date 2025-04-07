from django.db import models

class Transaction(models.Model):
    transaction_type = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_type

# Create your models here.
