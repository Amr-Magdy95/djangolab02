from django.urls import path 
from . import views 

app_name = "lab02app"

urlpatterns = [
    path('', views.index, name="index"),
    #Movie #C #R #U #D
    #Create
    path("view_form", views.view_form, name="movieform"),
    path("postmovie", views.movie_form, name="movie_form"),
    #Read
    path("<int:movie_id>/movie_details/", views.movie_details, name="movie_details"),
    #Update
    path("<int:movie_id>/update_movie/", views.update_movie, name="update_movie"),
    path("<int:movie_id>/confirm_update/", views.confirm_update, name="confirm_update"),
    #Delete
    path("<int:movie_id>/delete/", views.delete_movie, name="delete_movie")

]