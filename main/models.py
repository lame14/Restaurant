from django.db import models

# Модель бронирования столика
class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    comment = models.TextField(blank=True, default="")

    def __str__(self):  
        return f"{self.name} - {self.date} {self.time}"

# Модель отзыва
class Review(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.PositiveIntegerField()  # 1-5

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating}⭐"
    
class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ("main", "Основні страви"),
        ("salad", "Cалати"),
        ("soup", "Супи"),
        ("dessert", "Десерти"),
        ("drink", "Hanoї"),
    ]
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models. DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="main")
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='menu/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.price})"