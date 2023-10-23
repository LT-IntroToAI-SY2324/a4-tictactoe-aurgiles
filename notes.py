# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    def __init__(self, n = "", fc = "", a=0, ff=""):
        """create an instance of the dog class and set attributes"""
        self.name = n
        self.fur_color = fc
        self.age = a
        self.favorite_food = ff
        self.fetch_count = 0

    def __str__(self) -> str:
        """return a string representation of a dog"""
        s = "dogs name is " + str(self.name) + "\n"
        s += "and age is " + self.name + "\n"
        s += "and fur color is " + self.fur_color + "\n"
        s += "and they have played fetch " + str(self.fetch_count) + " times\n"
        return s

    def play_fetch(self, num_times):
        self.fetch_count += num_times

mydog = Dog("logan", "black", 7, "salmon")
chrisdog = Dog("luna", "black and white", 6, "tortillas")

print(mydog)
print(chrisdog)

mydog.play_fetch(20)
chrisdog.play_fetch(3)

print(mydog)
print(f"{chrisdog.name} has played fetch {chrisdog.fetch_count}")
