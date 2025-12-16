from coffee import Coffee
from milk_decorator import MilkDecorator
from sugar_decorator import SugarDecorator

coffee = Coffee()
coffee = MilkDecorator(coffee)
coffee = SugarDecorator(coffee)

print(coffee.cost())
