import addressbook_pb2

person = addressbook_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"

phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.PHONE_TYPE_HOME

# Serialize
with open("proto/person.pb", "wb") as f:
    data: bytes = person.SerializeToString()
    print(data)
    f.write(person.SerializeToString())

# Deserialize
person2 = addressbook_pb2.Person()
person2.ParseFromString(data)
print(person2)