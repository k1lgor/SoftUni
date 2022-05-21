from unittest import TestCase, main

from project.pet_shop import PetShop


class PetShopTests(TestCase):
    def setUp(self) -> None:
        self.pet = PetShop('manqk')

    def test_init(self):
        name = 'manqk'
        food = {}
        pets = []
        pet = PetShop(name)
        self.assertEqual(name, pet.name)
        self.assertEqual(food, pet.food)
        self.assertEqual(pets, pet.pets)

    def test_add_food_quantity(self):
        with self.assertRaises(ValueError) as ex:
            self.pet.add_food(self.pet.name, -2)
        self.assertEqual(
            'Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_not_in_foods(self):
        self.pet.add_food('hrana', 1)
        self.assertEqual({'hrana': 1}, self.pet.food)
        self.pet.add_food('hrana', 1)
        self.assertEqual({'hrana': 2}, self.pet.food)
        result = self.pet.add_food('hrana', 1)
        self.assertEqual('Successfully added 1.00 grams of hrana.', result)

    def test_add_pet_if_not_in_pets(self):
        result = self.pet.add_pet('kancho')
        self.assertEqual(['kancho'], self.pet.pets)
        self.assertEqual('Successfully added kancho.', result)
        with self.assertRaises(Exception) as ex:
            self.pet.add_pet('kancho')
        self.assertEqual(
            'Cannot add a pet with the same name', str(ex.exception))

    def test_feed_pet_if_pet_doesnt_exist(self):
        self.pet.pets = []
        with self.assertRaises(Exception) as ex:
            self.pet.feed_pet('hrana', 'kancho')
        self.assertEqual('Please insert a valid pet name', str(ex.exception))

    def test_feed_pet_if_food_doesnt_exist(self):
        self.pet.pets = ['manqk']
        self.pet.food = {}
        result = self.pet.feed_pet('hrana', self.pet.name)
        self.assertEqual('You do not have hrana', result)

    def test_feed_pet_if_food_less_than_100(self):
        self._extracted_from_test_feed_pet_if_food_more_than_100_2(
            90, 'Adding food...', 1090)

    def test_feed_pet_if_food_more_than_100(self):
        self._extracted_from_test_feed_pet_if_food_more_than_100_2(
            110, 'manqk was successfully fed', 10)

    # TODO Rename this here and in `test_feed_pet_if_food_less_than_100` and `test_feed_pet_if_food_more_than_100`
    def _extracted_from_test_feed_pet_if_food_more_than_100_2(self, arg0, arg1, arg2):
        self.pet.food = {'hrana': arg0}
        self.pet.pets = ['manqk']
        result = self.pet.feed_pet('hrana', 'manqk')
        self.assertEqual(arg1, result)
        self.assertEqual({'hrana': arg2}, self.pet.food)

    def test_repr(self):
        self.pet.name = 'manqk'
        self.pet.pets = ['kuche', 'kotka']
        result = self.pet.__repr__()
        self.assertEqual(f'Shop {self.pet.name}:\n'
                         f'Pets: {", ".join(self.pet.pets)}', result)


if __name__ == '__main__':
    main()
