from django.urls import path
from .views import home, explore, details, create, author

app_name="BaseSite"

urlpatterns = [
    path('', home, name="home"),
    path("/explore", explore, name="explore"),
    path("/details", details, name="details"),
    path("/create", create, name="create"),
    path("/author", author, name="author"),
]
