from unittest import TestCase, main

from project.movie import Movie


class MovieTests(TestCase):
    def test__init__when_have_happy_case(self):
        movie = Movie('marvel', 2020, 5.5)
        self.assertEqual('marvel', movie.name)
        self.assertEqual(2020, movie.year)
        self.assertEqual(5.5, movie.rating)

    def test__init__when_have_invalid_name(self):
        with self.assertRaises(ValueError) as context:
            movie = Movie('', 2020, 5.5)
        self.assertEqual("Name cannot be an empty string!",
                         str(context.exception))

    def test__init__when_have_invalid_year(self):
        with self.assertRaises(ValueError) as context:
            movie = Movie('marvel', 1780, 5.5)
        self.assertEqual("Year is not valid!", str(context.exception))

    def test__add_actor__when_exist_not_actor(self):
        movie = self._extracted_from_test__add_actor__when_exist_actor_2()
        movie.add_actor('ironman')
        self.assertEqual(['spiderman', 'ironman'], movie.actors)
        self.assertTrue('ironman' in movie.actors)

    def test__add_actor__when_exist_actor(self):
        movie = self._extracted_from_test__add_actor__when_exist_actor_2()
        result = movie.add_actor('spiderman')
        self.assertEqual(
            "spiderman is already added in the list of actors!", result)

    # TODO Rename this here and in `test__add_actor__when_exist_not_actor` and `test__add_actor__when_exist_actor`
    def _extracted_from_test__add_actor__when_exist_actor_2(self):
        result = Movie('marvel', 2020, 5.5)
        result.add_actor('spiderman')
        self.assertEqual(['spiderman'], result.actors)
        self.assertTrue('spiderman' in result.actors)
        return result

    def test__gt__when_first_is_bigger(self):
        self._extracted_from_test__gt__when_second_is_bigger_2(
            5.2, '"marvel" is better than "marvel2"')

    def test__gt__when_second_is_bigger(self):
        self._extracted_from_test__gt__when_second_is_bigger_2(
            5.8, '"marvel2" is better than "marvel"')

    # TODO Rename this here and in `test__gt__when_first_is_bigger` and `test__gt__when_second_is_bigger`
    def _extracted_from_test__gt__when_second_is_bigger_2(self, arg0, arg1):
        movie1 = Movie('marvel', 2020, 5.5)
        movie2 = Movie('marvel2', 2021, arg0)
        result = movie1.__gt__(movie2)
        self.assertEqual(arg1, result)

    def test__repr__when_valid(self):
        movie1 = Movie('marvel', 2020, 5.5)
        movie1.add_actor('spiderman')
        movie1.add_actor('ironman')
        expected = "Name: marvel\n" \
            "Year of Release: 2020\n" \
            "Rating: 5.50\n" \
            "Cast: spiderman, ironman"
        actual = movie1.__repr__()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
