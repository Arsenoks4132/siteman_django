from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from man.models import Man, Category
from .permissions import IsAdminOrReadOnly
from .serializers import ManSerializer


class ManAPIListPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 20


class ManAPIList(generics.ListCreateAPIView):
    queryset = Man.objects.all()
    serializer_class = ManSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ManAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Man.objects.all()
    serializer_class = ManSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication, )


class ManAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Man.objects.all()
    serializer_class = ManSerializer
    permission_classes = (IsAdminOrReadOnly,)
