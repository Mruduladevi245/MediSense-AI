class EmergencyContact:
    
    def __init__(self):

        self.contacts = []

    def add_contact(

        self,

        name,

        relation,

        phone

    ):

        contact = {

            "name": name,

            "relation": relation,

            "phone": phone

        }

        self.contacts.append(contact)

        return contact

    def remove_contact(self, phone):

        self.contacts = [

            c for c in self.contacts

            if c["phone"] != phone

        ]

    def get_contacts(self):

        return self.contacts