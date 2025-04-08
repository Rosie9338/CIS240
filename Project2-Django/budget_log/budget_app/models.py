from django.db import models

class Transaction(models.Model):
    transaction_type = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_type

class Entry(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    merchant = models.CharField(max_length=200)
    description = models.TextField()
    transaction_amount = models.FloatField(max_length=10)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Entries"

    def __str__(self):
        return self.merchant