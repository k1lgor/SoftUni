from unittest import TestCase, main

from project.team import Team


class TeamTests(TestCase):
    def setUp(self) -> None:
        name = 'BMW'
        self.team = Team(name)

    def test_init(self):
        name = 'BMW'
        self.assertEqual(name, self.team.name)
        self.assertEqual({}, self.team.members)

    def test_if_name_is_not_alpha(self):
        with self.assertRaises(ValueError) as ex:
            team = Team('123')
        self.assertEqual('Team Name can contain only letters!', str(ex.exception))

    def test_add_member_by_name(self):
        self.team.members['pesho'] = 20
        result = self.team.add_member(pesho=20, kancho=20)
        self.assertEqual('Successfully added: kancho', result)
        self.assertEqual(20, self.team.members['pesho'])
        self.assertEqual(20, self.team.members['kancho'])

    def test_remove_member_by_name_if_exists(self):
        self.team.members['pesho'] = 20
        self.team.members['kancho'] = 19

        result = self.team.remove_member('pesho')
        self.assertEqual('Member pesho removed', result)
        self.assertEqual(19, self.team.members['kancho'])
        self.assertTrue('pesho' not in self.team.members)

    def test_remove_member_by_name_if_doesnt_exist(self):
        result = self.team.remove_member('manqk')
        self.assertEqual('Member with name manqk does not exist', result)

    def test_gt(self):
        self.team.members['m1'] = 20
        self.team.members['m2'] = 21
        another_team = Team('AUDI')
        another_team.members['m1'] = 22
        another_team.members['m2'] = 23
        another_team.members['m3'] = 24
        self.assertEqual(True, another_team > self.team)
        self.assertEqual(False, another_team < self.team)

    def test_len_of_members(self):
        self.team.members['m1'] = 20
        self.team.members['m2'] = 20
        self.assertEqual(2, len(self.team.members))

    def test_add(self):
        self.team.members['m1'] = 18
        self.team.members['m2'] = 19
        another_team = Team('AUDI')
        another_team.members['m3'] = 20
        another_team.members['m4'] = 21
        another_team.members['m5'] = 22
        result = self.team + another_team
        expected = {
            'm1': 18,
            'm2': 19,
            'm3': 20,
            'm4': 21,
            'm5': 22
        }
        self.assertEqual('BMWAUDI', result.name)
        self.assertEqual(expected, result.members)

    def test_str(self):
        self.team.members['m2'] = 19
        self.team.members['m1'] = 18
        self.team.members['m3'] = 20
        result = str(self.team)
        expected = f'Team name: BMW\n' \
                   f'Member: m3 - 20-years old\n' \
                   f'Member: m2 - 19-years old\n' \
                   f'Member: m1 - 18-years old'
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
