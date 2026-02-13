from sabzeno.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            self.session['cart'] = {}
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'price': product.new_prices, "weight": product.weight}
        else:
            self.cart[product_id]['quantity'] += 1

        self.save()

    def decrease(self, product):
        product_id = str(product.id)
        if self.cart[product_id]['quantity'] > 0:
            self.cart[product_id]['quantity'] -= 1
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def clear(self):
        del self.session['cart']
        self.save()

    def get_post_price(self, product):
        weight = sum(item['weight'] * item['quantity'] for item in self.cart.values())
        if weight < 5000:
            return 20000
        elif weight < 10000:
            return 40000
        else:
            return 70000

    def total_price(self):
        price = sum(item['price'] * item['quantity'] for item in self.cart.values())
        return price

    def __len___(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart_dicts = self.cart.copy()
        for product in products:
            cart_dicts[str(product.id)]['product'] = product
        for item in cart_dicts.values():
            yield item
    def save(self):
        self.session.modified = True
