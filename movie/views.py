
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

# Create your views here.
from .forms import MovieForm
from .models import Movie
from django.http import HttpResponse
from django.core import serializers


def retrieve_view_movie(request):
    movie_list = Movie.objects.all()
    output = serializers.serialize('json', movie_list)
    return HttpResponse(output, content_type='application/json')


# def person_data(request):
#    Person_list = Person.objects.all()
#    output = serializers.serialize('json', Person_list)
#    return HttpResponse(output, content_type='application/json')


def create_view_movie(request):
    context = {}

    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_view_movie.html", context)


# def create_view_person(request):
#    context = {}

#    form = PersonForm(request.POST or None)
#   if form.is_valid():
#        form.save()
#
#    context['form'] = form
#    return render(request, "create_view_person.html", context)


def delete_view_movie(request, id):
    context = {}

    obj = get_object_or_404(Movie, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "delete_view_movie.html", context)


def detail_view_movie(request, id):
    context = {}

    context["data"] = Movie.objects.get(id=id)

    return render(request, "detail_view_movie.html", context)


def update_view_movie(request, id):
    context = {}

    obj = get_object_or_404(Movie, id=id)

    form = MovieForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    context["form"] = form

    return render(request, "update_view_movie.html", context)
