from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from .models import (
    Category,
    Subcategory,
    Product,
    ImageSet)


class ShopTestCases(TestCase):
    """ Класс проверки приложения shop """
    def setUp(self) -> None:
        self.category = Category.objects.create(title="Деревья")
        self.subcategory = Subcategory.objects.create(
            category=self.category,
            title="Хвойные")
        
    def test_create_subcategory(self):
        subcategory = Subcategory.objects.create(
            category=self.category,
            title="Лиственные")

    def test_create_product(self):
        image = SimpleUploadedFile(
            "trees_img.jpg",
            content=b'',
            content_type="image/jpg")
        self.product=Product.objects.create(
            category=self.category,
            subcategory=self.subcategory,
            title="Ёлка",
            description="Test tree",
            price=500,
            image=image)