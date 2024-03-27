def individual_serial(Registration)->dict:
    return{
        "id":str(Registration["_id"]),
        "username":str(Registration["username"]),
        "password":str(Registration["password"]),
        "email":str(Registration["email"]),
        "phone_number":str(Registration["phone_number"]),

    }

def list_serial(Registrations)->list:
    return [individual_serial(Registration=registration) for registration in Registrations]