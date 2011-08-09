from book.models import Book
from django.shortcuts import render_to_response


def list(request):
    ''' Listado de libros '''
    book_list = Book.objects.all()
    return render_to_response(
        'book/list.html',
        {'book_list': book_list}
    )


def get(request, book_slug):
    ''' Obtener un libro en particular '''
    book = Book.objects.get(slug_name=book_slug)
    return render_to_response(
        'book/get.html',
        {'book': book}
    )
