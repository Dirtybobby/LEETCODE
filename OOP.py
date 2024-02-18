class FootballPlayer:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def player_info(self):
        print(f"Player {self.name} {self.age} years old, salary: {self.salary}.")

     def __str__(self):
         return f"{self.name}, age: {self.age}, salary: {self.salary}."


ronaldinho = FootballPlayer("Ronaldinho", 40, 4_000_000)

ronaldinho.player_info()

print(ronaldinho)
