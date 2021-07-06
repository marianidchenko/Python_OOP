class PizzaDelivery:
    ordered = False
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient, quantity, price_per_ingredient):
        if not PizzaDelivery.ordered:
            extra_price = price_per_ingredient * quantity
            if ingredient in self.ingredients.keys():
                self.ingredients[ingredient] += quantity
            else:
                self.ingredients[ingredient] = quantity
            self.price += extra_price
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredient, quantity, price_per_ingredient):
        if not PizzaDelivery.ordered:
            price_drop = price_per_ingredient * quantity
            if ingredient not in self.ingredients.keys():
                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
            else:
                if self.ingredients[ingredient] < quantity:
                    return f"Please check again the desired quantity of {ingredient}!"
                else:
                    self.price -= price_drop
                    self.ingredients[ingredient] -= quantity
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"


    def make_order(self):
        ingredients = ', '.join([f'{ing}: {quantity}' for ing, quantity in self.ingredients.items()])
        PizzaDelivery.ordered = True
        return f"You've ordered pizza {self.name}"\
            f" prepared with {ingredients} and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
