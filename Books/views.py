from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Book, Authors

# Create your views here.

class BookDetailView(DetailView):
    model = Book
    template_name = 'onebook.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BooksListView(ListView):
    queryset = Book.book_coverObj.all()
    template_name = 'home.html'
    paginate_by = 6   

class AuthorDetailView(DetailView):
    model = Authors
    template_name = 'author.html'

