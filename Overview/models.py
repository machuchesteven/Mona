from django.db import models
from django.contrib.auth.models import User, UserManager

# this is a mona shopping app
# Models are Product, Order, Customer, Seller, Admin, and these models will have their managers
# The modal manager helps in making sure there is equivalence in real stock and in the Server Stock


class ProductCategory(models.Model):
    class Meta:
        verbose_name_plural = "Product Categories"
    id = models.AutoField(primary_key=True, default=1)
    name = models.CharField(max_length=32, unique=True, default=1)
    def __str__(self):
        return self.name
    

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    sold_quantity = models.PositiveIntegerField(default=0)
    # category = models.ForeignKey(ProductCategory, on_delete=models.SET_DEFAULT, null=True, default=1)
    pic = models.ImageField(upload_to="products/images/cover", blank=True)
    description = models.CharField(max_length=250, default="THis is used in assigning user friendly components into the material")

    def __str__(self):
        return self.name
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    time = models.TimeField(auto_now=True, auto_now_add=False)
    paid = models.BooleanField(default=False)


# class Delivery(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     time = models.TimeField(auto_now=False, auto_now_add=False)
#     arrival_time = models.TimeField(auto_now=False, auto_now_add=False)
#     delivered = models.BooleanField()

class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    products = models.PositiveIntegerField()
    ratings = models.DecimalField(max_digits=2, decimal_places=1)
    def __str__(self):
        return self.name

class Customer(models.Model):
    pass

class DailyOffer(models.Model):
    id = models.AutoField(primary_key=True)
    offer_title = models.CharField(max_length=64)
    offer_detail = models.CharField(max_length=200)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.offer_title

class Comment(models.Model):
    product = models.ForeignKey(Product,  on_delete=models.CASCADE)
    user = models.CharField(max_length=32)
    content = models.TextField()
    time_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} Comment by {self.user}"

