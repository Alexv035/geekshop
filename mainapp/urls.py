from django.urls import path

import mainapp.views as mainapp

app_name = "mainapp"

urlpatterns = [
    path("", mainapp.products, name="index"),
<<<<<<< HEAD
    path("category/<int:pk>/", mainapp.products, name="category"),
=======
    path("<int:pk>/", mainapp.products, name="category"),
>>>>>>> 5539558d9be13560ab5dc147173724041e4ec066
]
