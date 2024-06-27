from faker import Faker

def create_product_data():
    fake = Faker()
    return {
        'name': fake.word(),
        'price': str(fake.random_number(digits=2)),
        'description': fake.text(),
        'quantity': str(fake.random_number(digits=2))
    }