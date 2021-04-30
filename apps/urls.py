from django.urls import path
from .views import *

urlpatterns = [
    path('book_list/', book_list),
    path('select_related/', book_list_select_related),
    path('store_list/', store_list),
    path('prefetch_related/', store_list_prefetch_related),
    path('expensive/', store_list_expensive_books_prefetch_related),

    path('efficient/', store_list_expensive_books_prefetch_related_efficient)

]
