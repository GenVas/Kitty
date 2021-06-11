from django.urls import include, path

#from cats.views import cat_list
from cats.views import APICat, CatList, CatDetail

urlpatterns = [
#   path('cats/', cat_list, name='cat_list'), # Вариант 1
#   path('cats/', APICat.as_view()), # Вариант 2
    path('cats/', CatList.as_view()), # Вариант 3
    path('cats/<int:pk>/', CatDetail.as_view()), # Вариант 3 
]


