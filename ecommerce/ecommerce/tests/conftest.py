from pytest_factoryboy import register

from .factories import CategoryFactory, BrandFactory, ProductFactory

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)


# lemme test any other commits available ?
