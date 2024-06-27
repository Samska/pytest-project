from faker import Faker

def create_user_data():
    fake = Faker()
    return {
        'name': fake.name(),
        'email': fake.email(),
        'password': fake.password()
    }
