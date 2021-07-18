from faker import Faker
from faker.providers.phone_number.en_US import Provider as PhoneProvider
from faker.providers.person import Provider as PersonProvider

faker = Faker()
class DataFaker:
    def __init__(self):
        self.faker = Faker()
        self.phone_ru = PhoneProvider(self.faker)

    def get_last_name(self):
        return self.faker.last_name()

    def get_first_name(self):
        return faker.first_name()

    def get_address(self):
        return self.faker.address()

    def get_email(self):
        return self.faker.email()

    def get_post_code(self):
        return self.faker.random_int(10000, 19999)

    def get_phone(self):
        return "3457793457"

    def get_city(self):
        return self.faker.city()

    def get_password(self):
        return self.faker.password()
