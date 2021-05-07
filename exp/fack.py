from faker import Faker

fake = Faker(locale='zh_CN')
print(fake.address())
