from django.db import models


# Base menu
class Sandwich(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    calories = models.IntegerField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title

class Salad(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    calories = models.IntegerField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title

class Wrap(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    calories = models.IntegerField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title

class Side(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    calories = models.IntegerField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title

class Soup(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    calories = models.IntegerField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title

class Drink(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    calories = models.IntegerField()
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title

# Build your own options
class Bread(models.Model):
    title = models.CharField(max_length=30)
    calories = models.IntegerField()
    image = models.ImageField(blank=True)
    

    def __str__(self):
        return self.title

class Tortilla(models.Model):
    title = models.CharField(max_length=30)
    calories = models.IntegerField()
    image = models.ImageField(blank=True)
    
    def __str__(self):
        return self.title

class Lettuce(models.Model):
    title = models.CharField(max_length=30)
    calories = models.IntegerField()
    image = models.ImageField(blank=True)
   
    def __str__(self):
        return self.title
    
class Protein(models.Model):
    title = models.CharField(max_length=30)
    calories = models.IntegerField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title

class Topping(models.Model):
    title = models.CharField(max_length=30)
    calories = models.IntegerField()
    image = models.ImageField(blank=True)
   
    def __str__(self):
        return self.title
    





