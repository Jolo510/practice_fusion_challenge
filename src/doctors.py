class Doctor:
	""" Summary of class here.

		Doctor contains
			- num_id
			- name
			- specialty
			- area
			- score

		Attributes:
			similarity_score: Generates a similarity score between two doctors
	"""
	def __init__(self, num_id, name, specialty, area, score):
		self.num_id = num_id
		self.name = name
		self.specialty = specialty
		self.area = area
		self.score = score

	def similarity_score(self, comparing_doctor):
		""" Generates a similarity score

			Args:
				comparing_doctor: A doctor object to compare too

			Returns:
				A similarity score between the two doctors. Score ranges from 0 - 6
		"""
		score = 0
		score_points = {
			'specialty': 3,		# Largest factor because the doctors have the same profession
			'area': 2,
			'score': 1
		};

		if self.specialty == comparing_doctor.specialty:
			score += score_points['specialty']

		if self.area == comparing_doctor.area:
			score += score_points['area']

		# If two scores are in the same range (e.g 78 and 73 are in 70-79 range), full points are awarded
		comparing_score_range_difference = abs( (self.score // 10) - (comparing_doctor.score // 10) ) / 10

		score += score_points['score'] - comparing_score_range_difference

		return score

