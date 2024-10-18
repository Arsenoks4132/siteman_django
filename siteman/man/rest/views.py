from django.forms import model_to_dict
from django.utils.text import slugify

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from man.models import Man
from .serializers import ManSerializer


# class ManAPIView(generics.ListAPIView):
#     queryset = Man.published.all()
#     serializer_class = ManSerializer

# class ManAPIView(APIView):
#     def get(self, request):
#         w = Man.objects.all()
#         return Response({'posts': ManSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = ManSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Man.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = ManSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         # здесь код для удаления записи с переданным pk
#
#         return Response({"post": "delete post " + str(pk)})

# class ManAPIView(APIView):
#     def get(self, request):
#         lst = Man.published.all().values()
#         return Response({'mans': list(lst)})
#
#     def post(self, request):
#         post_new = Man.objects.create(
#             title=request.data['title'],
#             slug=slugify(request.data['title']),
#             content=request.data['content'],
#             cat_id=request.data['cat_id'],
#         )
#         return Response({'man': model_to_dict(post_new, fields=('title', 'content', 'cat_id'))})


class ManAPIList(generics.ListCreateAPIView):
    queryset = Man.published.all()
    serializer_class = ManSerializer


class ManAPIUpdate(generics.UpdateAPIView):
    queryset = Man.objects.all()
    serializer_class = ManSerializer

class ManAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Man.objects.all()
    serializer_class = ManSerializer