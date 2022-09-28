from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), #home page of app
    #path("persons/", views.members, name="Persons"),
    path("list/", views.tables, name="list" ), #list of members in database
    path("list/add/", views.add, name="add"), #url to add member to database
    path("list/add/addrecord/", views.addrecord, name="addrecord"),
    path("list/delete/<int:id>", views.delete, name="delete"),
    path("list/update/<int:id>", views.update, name="update"),
    path("list/update/updaterecord/<int:id>", views.updaterecord, name="updaterecord")
]