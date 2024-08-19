class Duck:
    def quack(self):
        print("Quack! I am a duck.")
class Goose:
    def quack(self):
        print("Quack! I am a goose.")
def make_quack(animal):
    if hasattr(animal, "quack"):  
        animal.quack()            
    else:
        print("This animal doesn’t quack.")
duck = Duck()
goose = Goose()
make_quack(duck)    # Output: Quack! I am a duck.
make_quack(goose)   # Output: Quack! I am a goose.
