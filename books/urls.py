from django.urls import path

from .views import (
    BookCreateView,
    BookDeleteView,
    BookDetailsView,
    BookListView,
    ReadingSessionCreateView,
)

urlpatterns = [
    path("list/", BookListView.as_view(), name="book_list"),
    path("create/", BookCreateView.as_view(), name="book_create"),
    path(
        "<uuid:book_id>/create_session/",
        ReadingSessionCreateView.as_view(),
        name="create_session",
    ),
    path("<uuid:book_id>/details/", BookDetailsView.as_view(), name="book_details"),
    path("<uuid:book_id>/delete/", BookDeleteView.as_view(), name="book_delete"),
]
