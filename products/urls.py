from django.urls import path
from . import views
app_name = "products"

urlpatterns = [
    path('', views.index, name="index"),
    path('addtocart/<int:productid>',
         views.addtocart, name="addtocarts")
    # path('new', views.newproducts),


]
