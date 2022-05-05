from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTests(TestCase):
    def test_init(self):
        vehicle = Vehicle(1, 2)
        self.assertEqual(1, vehicle.fuel)
        self.assertEqual(2, vehicle.horse_power)
        self.assertEqual(1, vehicle.capacity)
        self.assertEqual(1.25, vehicle.fuel_consumption)

    def test_drive(self):
        vehicle = Vehicle(1, 2)
        with self.assertRaises(Exception) as ex:
            vehicle.drive(1)
        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_drive_if_not_error(self):
        vehicle = Vehicle(5, 2)
        vehicle.drive(1)
        self.assertEqual(3.75, vehicle.fuel)

    def test_refuel(self):
        vehicle = Vehicle(5, 2)
        with self.assertRaises(Exception) as ex:
            vehicle.refuel(2)
        self.assertEqual('Too much fuel', str(ex.exception))

    def test_refuel_if_not_error(self):
        vehicle = Vehicle(5, 2)
        vehicle.drive(2)
        self.assertEqual(2.5, vehicle.fuel)
        vehicle.refuel(1)
        self.assertEqual(3.5, vehicle.fuel)

    def test_str(self):
        vehicle = Vehicle(5, 2)
        result = vehicle.__str__()
        self.assertEqual('The vehicle has 2 horse power with 5 fuel left and 1.25 fuel consumption', result)


if __name__ == '__main__':
    main()
