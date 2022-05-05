from unittest import TestCase, main

from project.student import Student


class StudentTests(TestCase):
    def setUp(self) -> None:
        self.student = Student('John', {
            'Web programming': ['note1', 'note2'],
            'DB basics': ['note3', 'note4']
        })

    def test_init_only_with_name(self):
        name = 'John'
        student = Student(name)
        self.assertEqual(name, student.name)
        self.assertEqual({}, student.courses)

    def test_init_with_courses(self):
        name = 'John'
        courses = {
            'Web programming': ['note1', 'note2'],
            'DB basics': ['note3', 'note4']
        }
        student = Student(name, courses)
        self.assertEqual(name, student.name)
        self.assertEqual(courses, student.courses)

    def test_enroll_with_already_enrolled_course_adds_notes(self):
        course = 'DB basics'
        result = self.student.enroll(course, ['new note'])
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(['note3', 'note4', 'new note'], self.student.courses[course])

    def test_enroll_with_new_course_and_adds_the_course_with_notes(self):
        course = 'Front End basics'
        notes = ['FE1', 'FE2']
        result = self.student.enroll(course, notes, 'Y')
        self.assertEqual('Course and course notes have been added.', result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual(notes, self.student.courses[course])

    def test_enroll_with_new_course_and_adds_the_course_with_notes_with_empty(self):
        course = 'Front End basics'
        notes = ['FE1', 'FE2']
        result = self.student.enroll(course, notes, '')
        self.assertEqual('Course and course notes have been added.', result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual(notes, self.student.courses[course])

    def test_enroll_with_new_course_without_notes(self):
        course = 'Front End basics'
        notes = ['FE1', 'FE2']
        result = self.student.enroll(course, notes, 'N')
        self.assertEqual('Course has been added.', result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual([], self.student.courses[course])

    def test_add_notes_in_existing_course(self):
        course = 'Web programming'
        notes = 'note3'
        result = self.student.add_notes(course, notes)
        self.assertEqual('Notes have been updated', result)
        self.assertEqual(['note1', 'note2', 'note3'], self.student.courses[course])

    def test_add_notes_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('Invalid course', 'random')
        self.assertEqual('Cannot add notes. Course not found.', str(ex.exception))

    def test_leave_course_removes_course_from_student(self):
        course = 'DB basics'
        result = self.student.leave_course(course)
        self.assertEqual('Course has been removed', result)
        self.assertTrue(course not in self.student.courses)
        self.assertTrue(len(self.student.courses) > 0)

    def test_leave_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('Invalid course')
        self.assertEqual('Cannot remove course. Course not found.', str(ex.exception))


if __name__ == '__main__':
    main()
