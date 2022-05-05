from unittest import TestCase, main

from project.mammal import Mammal


class MammalTests(TestCase):
    def test_initialization(self):
        mammal = Mammal('Pesho', 'Kon', 'Bbhrhr')
        self.assertEqual('Pesho', mammal.name)
        self.assertEqual('Kon', mammal.type)
        self.assertEqual('Bbhrhr', mammal.sound)

    def test_make_sound(self):
        mammal = Mammal('Pesho', 'Kon', 'Bbhrhr')
        result = mammal.make_sound()
        self.assertEqual('Pesho makes Bbhrhr', result)

    def test_get_kingdom(self):
        mammal = Mammal('Pesho', 'Kon', 'Bbhrhr')
        result = mammal.get_kingdom()
        self.assertEqual(result, mammal._Mammal__kingdom)

    def test_info(self):
        mammal = Mammal('Pesho', 'Kon', 'Bbhrhr')
        result = mammal.info()
        self.assertEqual('Pesho is of type Kon', result)

if __name__ == '__main__':
    main()
