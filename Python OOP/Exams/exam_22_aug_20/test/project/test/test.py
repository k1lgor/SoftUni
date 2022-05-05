from unittest import TestCase, main

from project.student_report_card import StudentReportCard


class StudentReportCardTests(TestCase):
    def setUp(self) -> None:
        self.student = StudentReportCard('pesho', 2)

    def test_init(self):
        self.assertEqual('pesho', self.student.student_name)
        self.assertEqual(2, self.student.school_year)
        self.assertEqual({}, self.student.grades_by_subject)

    def test_student_name_if_empty_name(self):
        with self.assertRaises(ValueError) as ex:
            self.student.student_name = ''
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_range_of_school_year(self):
        with self.assertRaises(ValueError) as ex:
            self.student.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_add_grade(self):
        self.student.add_grade('Math', 6)
        self.assertEqual({'Math': [6]}, self.student.grades_by_subject)
        self.student.add_grade('Math', 5)
        self.assertEqual({'Math': [6, 5]}, self.student.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.student.grades_by_subject['Math'] = [6, 6]
        self.student.grades_by_subject['Geo'] = [6, 6]
        result = self.student.average_grade_by_subject()
        self.assertEqual('Math: 6.00\nGeo: 6.00', result)

    def test_average_grade_for_all_subjects(self):
        self.student.grades_by_subject['Math'] = [6, 6]
        self.student.grades_by_subject['Geo'] = [6, 6]
        result = self.student.average_grade_for_all_subjects()
        self.assertEqual('Average Grade: 6.00', result)

    def test_repr(self):
        self.student.grades_by_subject['Math'] = [6, 6]
        self.student.grades_by_subject['Geo'] = [6, 6]
        result = self.student.__repr__()
        self.assertEqual('Name: pesho\n'
                         'Year: 2\n'
                         '----------\n'
                         'Math: 6.00\nGeo: 6.00\n'
                         '----------\n'
                         'Average Grade: 6.00', result)


if __name__ == '__main__':
    main()
