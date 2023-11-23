from rest_framework import mixins
from .serializers import *
from rest_framework import generics
from .models import *
from rest_framework import filters



class ProductList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SearchList(generics.ListCreateAPIView):
    def search(self, request):
        queryset = Product.objects.all()
        serializer_class = ProductsSerializer
        filter_backends = [filters.SearchFilter]
        search_fields = ['name', 'description']
