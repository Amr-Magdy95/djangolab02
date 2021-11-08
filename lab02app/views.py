from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse
from .models import Movie


def index(request):
    latest_movies = Movie.objects.order_by("-publication_date")
    context = {
        "latest_movies": latest_movies
    }
    return render(request, 'lab02app/index.html', context)

#Create
def view_form(request):
    return render(request, 'lab02app/postmovie.html',{})
def movie_form(request):
    if request.method == "POST":
        movie_name = request.POST.get("movie_name")
        pub_date = request.POST.get("pub_date")

        movie_object = Movie.objects.create(name=movie_name, publication_date = pub_date)
        movie_object.save()

        return redirect("lab02app:index")
        return HttpResponse( pub_date)

#Read
def movie_details(request, movie_id):
    movie = Movie.objects.get(pk = movie_id)
    context = {
        "movie": movie
    }
    return render(request, 'lab02app/displaymovie.html',context)
    #response = "you're looking at the result: {}".format(movie)
    #return HttpResponse(response)

#Update
def update_movie(request, movie_id):
    movie = Movie.objects.get(pk = movie_id)
    print(movie)
    context = {
    "movie": movie
    }
    return render(request, 'lab02app/onemovie.html',context)
def confirm_update(request, movie_id):
    if request.method == "POST":
        movie_name = request.POST.get("movie_name")
        pub_date = request.POST.get("pub_date")

        Movie.objects.filter(pk=movie_id).update(name=movie_name, publication_date = pub_date)

        return redirect("lab02app:index")
def delete_movie(request, movie_id):
    Movie.objects.filter(pk=movie_id).delete()
    return redirect("lab02app:index")

