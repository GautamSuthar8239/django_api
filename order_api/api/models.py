from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    ]

    customer_name = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Auto-update timestamp

    class Meta:
        verbose_name_plural = "Orders"  # Fix plural naming in Django Admin

    def __str__(self):
        return f"{self.customer_name} - {self.product_name} ({self.status})"
