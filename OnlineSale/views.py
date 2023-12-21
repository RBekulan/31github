
from rest_framework import generics, mixins
from .models import Product
from .serializers import ProductsSerializer


from rest_framework import generics, mixins
from .models import Product
from .serializers import ProductsSerializer

class ProductList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    API endpoint that allows viewing a list of products or creating a new product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

    def get(self, request, *args, **kwargs):
        """
        Get a list of products.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Create a new product.
        """
        return self.create(request, *args, **kwargs)


class ProductDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    API endpoint that allows viewing, updating, or deleting a specific product.
    """
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

    def get(self, request, *args, **kwargs):
        """
        Retrieve a specific product instance.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Update a specific product instance.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Delete a specific product instance.
        """
        return self.destroy(request, *args, **kwargs)

print('text')

