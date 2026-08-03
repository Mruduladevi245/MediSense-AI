class EmergencyProfile:
    
    def __init__(
        self,
        name,
        age,
        blood_group,
        allergies,
        diseases,
        medications,
        emergency_contact
    ):

        self.name = name
        self.age = age
        self.blood_group = blood_group
        self.allergies = allergies
        self.diseases = diseases
        self.medications = medications
        self.emergency_contact = emergency_contact

    def to_dict(self):

        return {

            "name": self.name,

            "age": self.age,

            "blood_group": self.blood_group,

            "allergies": self.allergies,

            "diseases": self.diseases,

            "medications": self.medications,

            "emergency_contact": self.emergency_contact

        }