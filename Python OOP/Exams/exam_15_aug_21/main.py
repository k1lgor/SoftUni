from project.bakery import Bakery

bakery = Bakery('random name')

print(bakery.add_drink('Water', 'Spring', 250, 'gorna banq'))
print(bakery.add_drink('Water', 'Mineral', 500, 'gorna banq'))
print(bakery.add_drink('Tea', 'Ice', 250, 'asd'))
print(bakery.add_table('OutsideTable', 55, 15))
print(bakery.reserve_table(10))
print(bakery.order_drink(55, 'Spring', 'Mineral', 'Ice', 'Cola', 'Fanta'))
print(bakery.leave_table(55))
