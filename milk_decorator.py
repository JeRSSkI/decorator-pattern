from coffee_decorator import CoffeeDecorator

class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 5
