from unittest import TestCase, main


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception("Not enough energy.")

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


class WorkerTests(TestCase):
    def test_worker_is_initialized(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual("Test", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_energy_is_incremented(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual(10, worker.energy)
        worker.rest()
        self.assertEqual(11, worker.energy)

    def test_error_is_raised(self):
        self._extracted_from_test_error_with_negative_2(0)

    def test_error_with_negative(self):
        self._extracted_from_test_error_with_negative_2(-1)

    # TODO Rename this here and in `test_error_is_raised` and `test_error_with_negative`
    def _extracted_from_test_error_with_negative_2(self, arg0):
        worker = Worker("Test", 100, arg0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_money_increased(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual(0, worker.money)
        worker.work()
        self.assertEqual(100, worker.salary)
        self.assertEqual(100, worker.money)
        worker.work()
        self.assertEqual(200, worker.money)

    def test_energy_is_decreased_after_work(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual(10, worker.energy)
        worker.work()
        self.assertEqual(9, worker.energy)
        worker.work()
        self.assertEqual(8, worker.energy)

    def test_get_info(self):
        worker = Worker("Test", 100, 10)
        result = worker.get_info()
        expected = "Test has saved 0 money."
        self.assertEqual(expected, result)
        worker.work()
        result = worker.get_info()
        expected = "Test has saved 100 money."
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
