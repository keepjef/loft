from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView


from corp.models import Category, Product, Image
from .serializers import ProductSerializer, PhotoShowSerializer, ProductSerializerThis, CategorySerializer


def show_genres(request):
    return render(request, "genres.html", {'genres': Category.objects.all()})


# class CategoryAPIView(APIView):
#
#     def get(self, request):
#         lst = Category.objects.all().values()
#         return Response({'categories': list(lst)})


# class ProductAPIView(APIView):
#
#     def get(self, request):
#         lst = Product.objects.all().values()
#         return Response({'products': list(lst)})
#
#
#     def post(self, request):
#         post_new = Product.objects.create(
#             title=request.data['title'],
#
#         )
#         return Response({'post': model_to_dict(post_new)})

# class ProductAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerThis


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ImageView(RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = PhotoShowSerializer
