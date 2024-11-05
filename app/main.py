class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])

    for person_data in people:
        person = Person.people[person_data["name"]]
        if "wife" in person_data and person_data["wife"]:
            person.wife = Person.people[person_data["wife"]]
        elif "husband" in person_data and person_data["husband"]:
            person.husband = Person.people[person_data["husband"]]

    return list(Person.people.values())
