from django.db import models


class ProductCategory(models.Model):
    objects = None
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    create_date = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = None
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='имя продукта',
        max_length=128,
    )
    image = models.ImageField(
        upload_to='products_images',
        blank=True,
    )
    short_desc = models.CharField(
        verbose_name='краткое описание',
        max_length=60,
        blank=True,
    )
    description = models.TextField(
        verbose_name='описание продуктов',
        blank=True,
    )
    price = models.DecimalField(
        verbose_name='цена продуктов',
        max_digits=8,
        decimal_places=2,
        default=0,
    )
    quantity = models.PositiveIntegerField(
        verbose_name='количество на складе',
        default=0,
    )

    def __str__(self):
        return f"{self.name} ({self.category.name})"