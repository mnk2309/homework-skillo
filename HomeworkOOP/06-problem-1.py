class Email:
    def __init__(self, title):
        self.title = title

    def __eq__(self, other):
        if self.title == other.title:
            return True
        return False

    def __ne__(self, other):
        if self.title != other.title:
            return True
        return False


email1 = Email("johndoe@mail.com")
email2 = Email("emilyheart@yahoo.com")
email3 = Email("johndoe@mail.com")

print(email1 == email2)
print(email1 == email3)
print(email2 == email3)

print(email1 != email2)
print(email1 != email3)
print(email2 != email3)