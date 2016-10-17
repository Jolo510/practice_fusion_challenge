This was a programming assignment from Practice Fusion

Summary of Assignment
 - Given a doctor, provides a list of similar doctors, in a prioritized order
 - Include unit tests


Doctor Class
 - num_id
 - name
 - specialty
 - area
 - score

def similarity_score(self, comparing_doctor)
 - Score based on what similar properties between two doctors
 - Specialty has biggest effect on similarity score
 - Review Score has the least effect similarity score

def similar_doctors_list(doctor, list_of_doctors):
 - Computes the similarity_score for every doctor in the list_of_doctors
 - Then stores the results in a list of tuples for sorting purposes


How To Run Unit Test from the command line:
	navigate to ../practice_fusion/src

	Unit Test for doctors.py
	- python3 doctors_tests.py -v
	Unit Test for similar_doctors.py
    - python3 similar_doctors_tests.py -v
