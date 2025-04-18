# main.py
from pet import Pet

def main():
    """Creates a pet and demonstrates its methods."""

    my_pet = Pet(name="Bruno")
    print(f"Creating pet: {my_pet.name}")

    my_pet.eat()
    print(f"{my_pet.name} is eating...")

    my_pet.play()
    print(f"{my_pet.name} is playing...")

    my_pet.sleep()
    print(f"{my_pet.name} is sleeping...")

    my_pet.train("roll over")
    my_pet.train("play dead")

    print(f"{my_pet.name}'s current status:")
    my_pet.get_status()
    my_pet.show_tricks()
    my_pet.get_mood()
    my_pet.pass_time(3)
  

    


if __name__ == "__main__":
    main()