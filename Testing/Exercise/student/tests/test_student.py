from unittest import TestCase, main
from Testing.Exercise.student.project.student import Student


class StudentTests(TestCase):
    def setUp(self):
        self.student = Student('name')

    def test_init_returns_correct_values(self):
        self.assertEqual("name", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_add_course_that_has_not_been_added(self):
        result = self.student.enroll("course1", "note1", "N")
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student.courses['course1'])

    def test_add_course_that_has_not_been_added_and_notes(self):
        result = self.student.enroll("course1", "note1")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual("note1", self.student.courses['course1'])

    def test_add_existing_course(self):
        self.student.enroll("course1", "n", "N")
        result = self.student.enroll("course1", "n")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(["n"], self.student.courses['course1'])

    def test_adding_notes_to_existing_course(self):
        self.student.enroll("course1", "n", "N")
        result = self.student.add_notes("course1", "notes")
        self.assertEqual(["notes"], self.student.courses["course1"])
        self.assertEqual("Notes have been updated", result)

    def test_adding_notes_to_non_existing_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("course1", "notes")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        self.assertEqual({}, self.student.courses)

    def test_leave_existing_course(self):
        self.student.enroll("course1", "n", "N")
        result = self.student.leave_course("course1")
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student.courses)

    def test_leave_non_existing_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("aaa")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
        self.assertEqual({}, self.student.courses)


if __name__ == '__main__':
    main()