from django.db import models

# Create your models here.
class Food(models.Model) :

    title = models.CharField(max_length=200,unique=True)
    CUISINE_OPTIONS = (
        ("Italian", "Italian"),
        ("Indian", "Indian"),
        ("Chinese", "Chinese"),
        ("Mexican", "Mexican"),
        ("Thai", "Thai"),
        ("Japanese", "Japanese"),
        ("Korean", "Korean"),
        ("Continental", "Continental"),
        ("Mediterranean", "Mediterranean"),
        ("French", "French"),
        ("American", "American")
    )

    cuisine = models.CharField(max_length=200,choices=CUISINE_OPTIONS,default="Indian")
    CATEGORY_OPTIONS = (
        ("veg","veg"),
        ("non-veg","non-veg")
    )
    category = models.CharField(max_length=200,choices=CATEGORY_OPTIONS,default="veg")
    price = models.PositiveIntegerField()
    MEAL_TYPE_OPTIONS = (
        ("breakfast", "breakfast"),
        ("lunch", "lunch"),
        ("dinner", "dinner"),
        ("snacks", "snacks"),
        ("dessert", "dessert"),
        ("beverages", "beverages"),
    )

    meal_type = models.CharField(max_length=200,choices=MEAL_TYPE_OPTIONS,default="snacks")