from django.contrib import admin
from .models import Sandwich, Salad, Wrap, Side, Soup, Drink, Topping, Lettuce, Protein, Tortilla, Bread


admin.site.register(Sandwich)
admin.site.register(Wrap)
admin.site.register(Salad)
admin.site.register(Side)
admin.site.register(Soup)
admin.site.register(Drink)
# admin.site.register(BYO_Wrap)
# admin.site.register(BYO_Sandwich)
# admin.site.register(BYO_Salad)
admin.site.register(Topping)
admin.site.register(Lettuce)
admin.site.register(Protein)
admin.site.register(Tortilla)
admin.site.register(Bread)
