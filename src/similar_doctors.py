from doctors import Doctor

"""
	Creating a list of doctors to use as the data set.
"""
list_of_doctors = [
	Doctor('1', 'Dr.Myers', 'Anesthesiologist', 'Palo Alto', 100),
	Doctor('2', 'Dr.Jack', 'Dermatologist', 'Mountain View', 35),
	Doctor('3', 'Dr.Thompson', 'Endocrinologist', 'Palo Alto', 25),
	Doctor('4', 'Dr.Lebron', 'Microbiologist', 'Fremont', 46),
	Doctor('5', 'Dr.Curry', 'Neonatologist', 'Fremont', 76),
	Doctor('6', 'Dr.Johnson', 'Surgeon', 'Union City', 78),
	Doctor('7', 'Dr.Jordan', 'Radiologist', 'Palo Alto', 96),
	Doctor('8', 'Dr.Lin', 'Surgeon', 'Palo Alto', 84)
]

def similar_doctors_list(doctor, list_of_doctors):
	""" Returns a list of similar doctors

	Args:
		doctor: The Doctor we are trying to find similiar doctors too
		list_of_doctors: Our dataset of doctors

	Returns:
		A list of doctors that are similar to doctor passed in.
		Sorted by decreasing similarity
	"""
	similar_doctors = []
	# Generating an silmilarity score for each doctor
	# Storing the results in a list of tuples
	for doc in list_of_doctors:
		similar_doctors.append( (doctor.similarity_score(doc), str(doc)) )

	# Sort the simliar doctors based on the score
	similar_doctors.sort(key=lambda tup: tup[0], reverse=True)

	ranked_simularity =[]
	for current in similar_doctors:
		ranked_simularity.append(current[1])

	return ranked_simularity

