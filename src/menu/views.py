"""
imports the generic class based views from django rest framework
"""
from rest_framework import generics

from .models import (
    Sandwich, Salad,
    Wrap, Side,
    Soup, Drink,
    Topping, Lettuce,
    Protein, Tortilla,
    Bread
    )

from .serializers import (
    SandwichSerializer, SaladSerializer,
    WrapSerializer, SideSerializer,
    SoupSerializer, DrinkSerializer,
    ToppingSerializer, LettuceSerializer,
    ProteinSerializer, TortillaSerializer,
    BreadSerializer
)

class SandwichList(generics.ListAPIView):
    """This uses the generic ListAPIView to list all of the objects in this class"""
    queryset = Sandwich.objects.all()
    serializer_class = SandwichSerializer

class SaladList(generics.ListAPIView):
    queryset = Salad.objects.all()
    serializer_class = SaladSerializer

class WrapList(generics.ListAPIView):
    queryset = Wrap.objects.all()
    serializer_class = WrapSerializer

class SideList(generics.ListAPIView):
    queryset = Side.objects.all()
    serializer_class = SideSerializer

class SoupList(generics.ListAPIView):
    queryset = Soup.objects.all()
    serializer_class = SoupSerializer

class DrinkList(generics.ListAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

class ToppingList(generics.ListAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer

class LettuceList(generics.ListAPIView):
    queryset = Lettuce.objects.all()
    serializer_class = LettuceSerializer

class ProteinList(generics.ListAPIView):
    queryset = Protein.objects.all()
    serializer_class = ProteinSerializer

class TortillaList(generics.ListAPIView):
    queryset = Tortilla.objects.all()
    serializer_class = TortillaSerializer

class BreadList(generics.ListAPIView):
    queryset = Bread.objects.all()
    serializer_class = BreadSerializer





