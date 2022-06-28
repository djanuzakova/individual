from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from .filters import ProductPriceFilter



from .models import Product
from .serializers import ProductSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = ProductPriceFilter
    search_fields = ['title', 'description']

    def get_serializer_context(self):
        return {'request': self.request}


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

