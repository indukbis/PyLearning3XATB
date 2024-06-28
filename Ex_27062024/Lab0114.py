class Person:
    # Attributes
    name = None
    id = None
    age = None
    phone_number = None

    # behaviour
    def talk(self):  # no arg no return
        print("I can talk")

    def sleep(self, name):  # 1 arg, No return
        print("I am a method!!")
        print("sleep", name)

    def sleep2(self, name):  # 1 arg, 1 return
        print("I am a method!!")
        return None

    def walk(self):
        print("I am walking")

    def walk_return(self):  # no arg, 1 return
        return "I am walking"


# Create object of the person class
# objectRef = Object - className()
surya = Person()
surya.name = "surya prakash"
surya.talk()

Indu = Person()
Indu.name = "Indu K"
Indu.walk()
