class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # 0 = full, 10 = starving
        self.energy = 5  # 0 = tired, 10 = fully rested
        self.happiness = 5  # 0 = sad, 10 = very happy
        self.tricks = []  # For bonus 

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} has eaten. Hunger: {self.hunger}, Happiness: {self.happiness}")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} slept well. Energy: {self.energy}")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played! Energy: {self.energy}, Happiness: {self.happiness}, Hunger: {self.hunger}")
        else:
            print(f"{self.name} is too tired to play. Let them sleep first.")

    def get_status(self):
        print(f"\n🔎 {self.name}'s Status:")
        print(f"Hunger😋: {self.hunger}/10")
        print(f"Energy💪: {self.energy}/10")
        print(f"Happiness🥳: {self.happiness}/10")

    # BONUS 
    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
