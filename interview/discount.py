class DiscountTags:
    def __init__(self, products, discounts):
        self.products = products
        self.discounts = discounts
        self.price = 0

    def type_price(self, d_type, current_price, price, quantity):
        if d_type == '1':
            current_price.append(self.type_1(price, quantity))
        elif d_type == '2':
            current_price.append(self.type_2(price, quantity))
        else:
            current_price.append(price)

        return current_price

    def discount_price(self, product):
        current_price = []
        d_name, d_type, quantity = self.discounts[0]
        d_name1, d_type1, quantity1 = self.discounts[1]
        price = int(product[0])
        for d in product[1:]:
            if d == d_name:
                self.type_price(d_type, current_price, price, quantity)
            elif d == d_name1:
                self.type_price(d_type1, current_price, price, quantity1)
            else:
                current_price.append(price)
        return min(current_price)

    def type_1(self, price, percent):
        return price - price * (int(percent) / 100)

    def type_2(self, price, percent):
        return price - int(percent)

    def final_price(self):
        for product in self.products:
            self.price += self.discount_price(product)
        return self.price


prod = [['10', 'd0', 'd1', 'd0'], ['15', 'd3', 'EMPTY'], ['20', 'd1', 'EMPTY']]
disc = [['d0', '1', '27'], ['d1', '2', '5'], ['d3', "0", '15']]
discount = DiscountTags(prod, disc)
print(discount.final_price())
