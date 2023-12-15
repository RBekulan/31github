from rest_framework import generics, mixins
from .models import CarOnline
from .serializers import CarOnlineSerializer


class CarList(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):
    """
    API endpoint that allows viewing a list of cars or creating a new car online.
    """
    queryset = CarOnline.objects.all()
    serializer_class = CarOnlineSerializer

    def get(self, request, *args, **kwargs):
        """
        Get a list of cars online.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Create a new car online.
        """
        return self.create(request, *args, **kwargs)


class CarDetail(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    """
    API endpoint that allows viewing, updating, or deleting a specific car online.
    """
    queryset = CarOnline.objects.all()
    serializer_class = CarOnlineSerializer

    def get(self, request, *args, **kwargs):
        """
        Retrieve a specific car online instance.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Update a specific car online instance.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Delete a specific car online instance.
        """
        return self.destroy(request, *args, **kwargs)
