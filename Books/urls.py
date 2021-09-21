from django.urls import path
from .views import AuthorDetailView, BookDetailView, BooksListView
from django.conf.urls.static import static
from django.conf import settings


app_name = 'Books'

urlpatterns = [
    path('', BooksListView.as_view(), name='Home'),
    path('book/<slug:slug>/', BookDetailView.as_view(), name='Book'),
    path('author/<slug:slug>/', AuthorDetailView.as_view(), name='Author'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)