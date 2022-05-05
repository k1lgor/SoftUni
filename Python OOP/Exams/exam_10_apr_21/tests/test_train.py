from unittest import TestCase, main

from project.train.train import Train


class TrainTests(TestCase):
    def setUp(self) -> None:
        self.train = Train('Loko', 2)

    def test_init(self):
        self.assertEqual('Loko', self.train.name)
        self.assertEqual(2, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_passengers_full(self):
        self.train.passengers = ['pass1', 'pass2']
        with self.assertRaises(ValueError) as ex:
            self.train.add('pass3')
        self.assertEqual("Train is full", str(ex.exception))

    def test_add_passengers(self):
        result = self.train.add('pass1')
        self.assertEqual(1, len(self.train.passengers))
        self.assertEqual('Added passenger pass1', result)

    def test_add_passengers_if_exist(self):
        self.train.add('pass1')
        with self.assertRaises(ValueError) as ex:
            self.train.add('pass1')
        self.assertEqual("Passenger pass1 Exists", str(ex.exception))

    def test_remove_passenger_if_exists(self):
        self.train.passengers = ['pass1', 'pass2']
        result = self.train.remove('pass1')
        self.assertEqual(['pass2'], self.train.passengers)
        self.assertEqual(1, len(self.train.passengers))
        self.assertEqual("Removed pass1", result)

    def test_remove_passenger_if_doesnt_exist(self):
        self.train.passengers = ['pass1', 'pass2']
        with self.assertRaises(ValueError) as ex:
            self.train.remove('pass3')
        self.assertEqual("Passenger Not Found", str(ex.exception))


if __name__ == '__main__':
    main()
