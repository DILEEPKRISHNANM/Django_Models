from django.shortcuts import render

from .models import Book
from django.http import Http404
from django.db.models import Avg

# Create your views here.


def index(request):


    books = Book.objects.all()

    num_books = books.count()

    average = books.aggregate(Avg("rating"))

    return render(request,"book_outlet/index.html",
    {
        "books":books,
        "num_books":num_books,
        "rating_average":average
    })



def book_detail(request,slug):
    try:

        book = Book.objects.get(slug=slug)
    except:
        raise Http404()

    return render(request,"book_outlet/book_detail.html",{
        "title":book.title,
        "author":book.author,
        "rating":book.rating,
        "is_bestselling":book.is_bestselling,
        "slugf":book.slug
    })




