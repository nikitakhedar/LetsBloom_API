from django.urls import path
from api import views
urlpatterns = [
    path('GET/api/books',views.get_api_books),
    path('POST/api/books',views.post_api_books),
    path('PUT/api/books',views.put_api_books)
]