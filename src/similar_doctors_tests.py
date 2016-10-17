import unittest
from similar_doctors import similar_doctors_list
from doctors import Doctor

class TestSimilarDoctor(unittest.TestCase):

	def test_simliar_doctors(self):
		doctors_list = [
			Doctor('1', 'Dr.Myers', 'Anesthesiologist', 'Palo Alto', 100),
			Doctor('2', 'Dr.Jack', 'Dermatologist', 'Fremont', 35),
			Doctor('3', 'Dr.Thompson', 'Endocrinologist', 'Palo Alto', 25)
		]

		comparing_doctor = Doctor('1', 'Dr.Rogers', 'Anesthesiologist', 'Fremont', 87)

		similar_list = similar_doctors_list(comparing_doctor, doctors_list)

		self.assertEqual(similar_list[0], 'ID: 1 Name: Dr.Myers Specialty: Anesthesiologist Area: Palo Alto Score: 100')
		self.assertEqual(similar_list[1], 'ID: 2 Name: Dr.Jack Specialty: Dermatologist Area: Fremont Score: 35')
		self.assertEqual(similar_list[2], 'ID: 3 Name: Dr.Thompson Specialty: Endocrinologist Area: Palo Alto Score: 25')

if __name__ == '__main__':
    unittest.main()