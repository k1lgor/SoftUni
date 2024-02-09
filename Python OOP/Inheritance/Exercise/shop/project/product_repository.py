from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        if (product := self.find(product_name)) is not None:
            self.products.remove(product)

    def __repr__(self):
        return ''.join(
            f'{product.name}: {product.quantity}\n' for product in self.products
        ).strip()
