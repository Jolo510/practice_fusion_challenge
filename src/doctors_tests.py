import unittest

from doctors import Doctor

class TestDoctorMethods(unittest.TestCase):

	def test_similarity_score(self):
		doctor_one = Doctor('1', 'Dr.Bob', 'Anesthesiologist', 'Palo Alto', 100)
		doctor_two = Doctor('2', 'Dr.Myers', 'Dermatologist', 'Palo Alto', 65)
		doctor_three = Doctor('3', 'Dr.Lynn', 'Dentist', 'Mountain View', 0)

		# Comparing the same doctor with itself should recieve max score
		self.assertEqual(doctor_one.similarity_score(doctor_one), 6)

		# Location in common
		self.assertEqual(doctor_one.similarity_score(doctor_two), 2.6)

		# Nothing in common
		self.assertEqual(doctor_one.similarity_score(doctor_three), 0)

	def test_str(self):
		doctor = Doctor('3', 'Dr.Lynn', 'Dentist', 'Mountain View', 0)
		self.assertEqual( str(doctor), 'ID: 3 Name: Dr.Lynn Specialty: Dentist Area: Mountain View Score: 0')

if __name__ == '__main__':
    unittest.main()