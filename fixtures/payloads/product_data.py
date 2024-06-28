from faker import Faker

def create_product_data():
    fake = Faker()
    return {
        'nome': fake.word(),
        'preco': str(fake.random_number(digits=2)),
        'descricao': fake.text(),
        'quantidade': str(fake.random_number(digits=2))
    }