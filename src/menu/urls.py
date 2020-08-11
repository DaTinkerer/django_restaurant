from .views import(
    SandwichList, SaladList,
    SoupList, SideList,
    DrinkList, BreadList,
    ProteinList, ToppingList,
    LettuceList, WrapList,
    TortillaList
)
from django.urls import path

app_name = 'menu'

urlpatterns = [
    path('sandwiches/', SandwichList.as_view()),
    path('salads/', SaladList.as_view()),
    path('wraps/', WrapList.as_view()),
    path('sides/', SideList.as_view()),
    path('soup/', SoupList.as_view()),
    path('drinks/', DrinkList.as_view()),
]