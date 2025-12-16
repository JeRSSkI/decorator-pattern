from coffee_decorator import CoffeeDecorator

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 2
