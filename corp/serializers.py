from rest_framework import serializers
from corp.models import Product, Image, Material, Category, Tag


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class PhotoShowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = "__all__"


class ProductSerializerThis(serializers.HyperlinkedModelSerializer):
    images = PhotoShowSerializer(read_only=True, many=True)
    materials = MaterialSerializer(read_only=True, many=True)
    categories = CategorySerializer(read_only=True, many=True)
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('title', 'price', 'description', 'images', 'width', 'length', 'height', 'materials', 'slug', 'alias', 'categories', 'tags')