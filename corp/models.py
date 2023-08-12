from django.db import models
from slugify import slugify

# from autoslug import AutoSlugField
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    text = models.CharField(max_length=200, default=None, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(default="category_images/default.png")

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
         return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)



class Material(models.Model):
    name = models.CharField(max_length=50, unique=True)



    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"

    def __str__(self):
         return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Метка"
        verbose_name_plural = "Метки"

    def __str__(self):
         return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)


class Product(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    price = models.IntegerField()
    width = models.CharField(max_length=200)
    length = models.CharField(max_length=200)
    height = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    materials = models.ManyToManyField(Material)
    images = models.ManyToManyField("Image")
    slug = models.SlugField(max_length=255, unique=True)

    alias = models.CharField(max_length=50, unique=True)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = "Карточка продукта"
        verbose_name_plural = "Карточки продуктов"

    def __str__(self):
         return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)


class Image(models.Model):

    image = models.ImageField(upload_to="product_images/", default="product_images/default.png")
    alt = models.CharField(max_length=255, default=None)

    def __str__(self):
         return self.alt