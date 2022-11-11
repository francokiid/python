# PYTHON OOP PRACTICE
# THIS PROGRAM RUNS, BUT IT IS UNFINISHED.
# INSPIRED BY RICK RIORDAN'S PERCY JACKSON BOOK SERIES


OlympianGods = {"Zeus":1, "Hera":2, "Poseidon":3, "Demeter":4, "Ares":5, "Athena":6,
"Apollo":7, "Artemis":8, "Hephaestus":9, "Aphrodite":10, "Hermes":11, "Dionysus":12, }


class GodParent:
    def __init__(self, godName, godTitle):
        self.godName = godName
        self.godTitle = godTitle


class HumanParent:
    def __init__(self, humanName):
        self.humanName = humanName


class Camper(GodParent, HumanParent):
    def __init__(self, camperName, camperAge, camperItem, godName, godTitle, humanName):
        self.camperName = camperName
        self.camperAge = camperAge
        self.camperItem = camperItem
        GodParent.__init__(self, godName, godTitle)
        HumanParent.__init__(self, humanName)

    def getCamperInfo(self):
        return [self.camperName.title(), self.camperAge, self.camperItem.title(), self.godName.title(), self.godTitle.title(), self.humanName.title()]


class Camp:
    def __init__(self):
        self.campers = []
    
    def showCamperInfo(self, i):
        print("\nDEMIGOD INFORMATION\n")
        print("Name:", self.campers[i][0])
        print("Age:", self.campers[i][1])
        print("Item:", self.campers[i][2])
        print("God Parent:", self.campers[i][3])
        print("Title of God Parent:", self.campers[i][4])
        print("Human Parent:", self.campers[i][5])
    
    def editCabins(self):
        pass


class Main:
    def __init__(self):
        self.campers = []

    def menu(self):
        while True:
            print("\n================================================")
            print("             WELCOME TO CAMP HALF-BLOOD")
            print("                 A Camp for Demigods")
            print("================================================\n")

            print("[1] Add a New Camper")
            print("[2] Show Camp Records")
            print("[3] Edit Camp Records")
            print("[4] Check Cabins")
            print("[5] Exit")

            choice = input("\nEnter choice ---> ")

            print("\n=================================================\n")

            if choice == "1":
                self.add()
            elif choice == "2":
                self.show()
            elif choice == "3":
                self.edit()
            elif choice == "4":
                self.check()
            elif choice == "5":
                print("Goodbye!\n")
                break
            else:
                print("Invalid input. Please try again.\n")
    
    def add(self):
        print("Fill in the required information to register.")
        name = input("Enter Name: ")
        while True:
            try:
                age = int(input("Enter Age: "))
                break
            except ValueError:
                print("Oops! Invalid input. Please try again.") 
        item = input("Enter Demigod Item: ")
        god = input("Enter God Parent Name: ")
        title = input("Enter Title of God Parent: ")
        human = input("Enter Human Parent Name: ")

        if name not in self.campers:
            self.campers.append(Camper(name, age, item, god, title, human).getCamperInfo())
            print("\nCamp Registration Successful!")

    def show(self):
        print(f"TOTAL NUMBER OF CAMPERS: {len(self.campers)}")
        num = 1
        for i in self.campers:
            print("[", num, "] ", i[0], "child of", i[3]) 
            num += 1
        if len(self.campers) > 0:
            self.showProfile()

    def showProfile(self):
        choice = input("\nView camper profile? [y] yes [n] no\nEnter choice >>> ")
        if choice.lower() == "y":
            print("\n=================================================\n")
            while True:
                try:
                    i = int(input("Enter camper number: "))
                    if i <= len(self.campers):
                        i -= 1
                        Camp.showCamperInfo(self, i)
                    else:
                        print(f"Camper #{i} does not exist.")
                    break
                except ValueError:
                    print("Invalid input. Please try again.")
        elif choice.lower() == "n":
            pass
        else:
            print("Oops! Invalid input.")

    def edit(self):
        pass

    def check(self):
        pass

if __name__ == "__main__":
    run = Main()
    run.menu()
