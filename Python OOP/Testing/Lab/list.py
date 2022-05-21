from unittest import TestCase, main


class IntegerList:
    def __init__(self, *args):
        self.__data = [x for x in args if type(x) == int]

    def get_data(self):
        return self.__data

    def add(self, element):
        if type(element) != int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif type(el) != int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


class IntegerListTest(TestCase):
    def test_constructor(self):
        integer = IntegerList()
        self.assertEqual([], integer._IntegerList__data)

    def test_wrong_data(self):
        integer = IntegerList('asd', '5.6')
        self.assertEqual([], integer._IntegerList__data)

    def test_correct_data(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer._IntegerList__data)

    def test_get_data(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer._IntegerList__data)
        result = integer.get_data()
        self.assertEqual([5], result)

    def test_add(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer._IntegerList__data)
        with self.assertRaises(ValueError) as ex:
            integer.add('5')
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_add_correct_data(self):
        integer = IntegerList(5)
        self.assertEqual([5], integer._IntegerList__data)
        integer.add(10)
        self.assertEqual([5, 10], integer._IntegerList__data)

    def test_remove_el_removes_element(self):
        integer = IntegerList(5)
        integer.remove_index(0)
        self.assertEqual([], integer._IntegerList__data)
        self.assertEqual(0, len(integer._IntegerList__data))

    def test_remove_invalid_idx(self):
        integer = IntegerList(5)
        with self.assertRaises(IndexError) as ex:
            integer.remove_index(2)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_remove_returns_element(self):
        integer = IntegerList(5)
        result = integer.remove_index(0)
        self.assertEqual(5, result)

    def test_get(self):
        integer = IntegerList(5)
        with self.assertRaises(IndexError) as ex:
            integer.get(2)
        self.assertEqual('Index is out of range', str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            integer.get(1)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_get_returns(self):
        integer = IntegerList(5)
        result = integer.get(0)
        self.assertEqual(5, result)

    def test_insert_invalid_idx(self):
        self._extracted_from_test_insert_invalid_data_type_2(
            IndexError, 2, 10, 'Index is out of range')

    def test_insert_invalid_data_type(self):
        self._extracted_from_test_insert_invalid_data_type_2(
            ValueError, 0, '10', 'Element is not Integer')

    # TODO Rename this here and in `test_insert_invalid_idx` and `test_insert_invalid_data_type`
    def _extracted_from_test_insert_invalid_data_type_2(self, arg0, arg1, arg2, arg3):
        integer = IntegerList(5)
        with self.assertRaises(arg0) as ex:
            integer.insert(arg1, arg2)
        self.assertEqual(arg3, str(ex.exception))

    def test_insert_adds_ele(self):
        integer = IntegerList(5)
        integer.insert(0, 10)
        self.assertEqual([10, 5], integer._IntegerList__data)

    def test_get_biggest(self):
        integer = IntegerList(5, -2, 100)
        result = integer.get_biggest()
        self.assertEqual(100, result)

    def test_get_index(self):
        integer = IntegerList(5, -2, 100)
        result = integer.get_index(-2)
        self.assertEqual(1, result)
        result = integer.get_index(100)
        self.assertEqual(2, result)


if __name__ == '__main__':
    main()
