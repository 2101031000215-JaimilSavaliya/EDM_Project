from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Attachment(models.Model):
    image = models.ImageField(upload_to="product")

    def __str__(self):
        return str(self.image)


class Product(models.Model):
    title = models.CharField(max_length=256)
    price = models.FloatField()
    old_price = models.FloatField(default=0.0)
    colors = models.CharField(max_length=32)
    size = models.CharField(max_length=32)
    product_details = models.TextField()
    details_care = models.TextField()
    delivery_returns = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    attachment = models.ManyToManyField(Attachment)

    def __str__(self):
        return f"{self.title}-{self.category}"
