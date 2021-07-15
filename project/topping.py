class Topping:
    def __init__(self, topping_type, weight):
        if not topping_type:
            raise ValueError("The topping type cannot be an empty string")
        else:
            self.topping_type = topping_type
        if weight <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        else:
            self.weight = weight


