import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_string_method(self, category_factory):
        x = category_factory()
        assert x.__str__() == "test_category"


class TestBrandModel:
    def test_string_method(self, brand_factory):
        x = brand_factory(name="overide_name")
        assert x.__str__() == "overide_name"


class TestProductModel:
    def test_string_method(self, product_factory):
        x = product_factory(name="overide_product")
        assert x.__str__() == "overide_product"
