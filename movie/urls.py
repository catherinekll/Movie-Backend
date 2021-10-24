from django.urls import path

from . import views

urlpatterns = [
    path('', views.retrieve_view_movie, name="Retrieve"),
    #path('person', views.person_data, name="person_data"),
    #path('person/create', views.create_view_person, name="create_view_person"),
    path('<id>', views.detail_view_movie, name="Detail"),
    path('create', views.create_view_movie, name='Create'),
    path('<id>/delete', views.delete_view_movie, name="Delete"),
    path('<id>/update', views.update_view_movie, name="Update"),
]
