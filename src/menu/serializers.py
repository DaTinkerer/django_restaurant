"""
imports the serializer classes from django rest framework
"""
from rest_framework import serializers

from .models import (
    Sandwich, Salad,
    Wrap, Side,
    Soup, Drink,
    Topping, Lettuce,
    Protein, Tortilla,
    Bread
    )

# Base Menu
class SandwichSerializer(serializers.ModelSerializer):
    """
    takes data from model class and serializes it to be formatted in JSON
    """
    
    class Meta:
        model = Sandwich
        fields = ['id', 'title', 'description', 'price', 'calories', 'image']


class SoupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soup
        fields = ['id', 'title', 'description', 'price', 'calories', 'image']

class SaladSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salad
        fields = ['id', 'title', 'description', 'price', 'calories', 'image']

class WrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wrap
        fields = ['id', 'title', 'description', 'price', 'calories', 'image']


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'title', 'description', 'price', 'calories', 'image']

class SideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Side
        fields = ['id', 'title', 'description', 'price', 'calories', 'image']

# Byo options
class ProteinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protein
        fields = ['id', 'title', 'price', 'calories', 'image']

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ['id', 'title', 'calories', 'image']

class LettuceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lettuce
        fields = ['id', 'title', 'calories', 'image']

class BreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bread
        fields = ['id', 'title', 'calories', 'image']

class TortillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tortilla
        fields = ['id', 'title', 'calories', 'image']




