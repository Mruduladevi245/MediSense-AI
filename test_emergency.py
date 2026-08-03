from emergency.emergency_profile import EmergencyProfile
from emergency.qr_generator import QRGenerator
from emergency.emergency_pdf import EmergencyPDF

profile = EmergencyProfile(
    name="John Doe",
    age=25,
    blood_group="O+",
    allergies="Penicillin",
    diseases="Diabetes",
    medications="Metformin",
    emergency_contact="9876543210"
)

data = profile.to_dict()

print(data)

print(QRGenerator.generate(data, "emergency_qr.png"))
print(EmergencyPDF.create(data))