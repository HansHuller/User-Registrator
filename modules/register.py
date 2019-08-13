import modules.data as dv


def register():
    while True:
        try:
            file = open("G:\\Hans Documents\\dev\\User-Registrator\\users.txt")
        except Exception:
            file = open("G:\\Hans Documents\\dev\\User-Registrator\\users.txt", "w")
            #print("Arquivo Criado")
            path = 1
        else:
            file = open("G:\\Hans Documents\\dev\\User-Registrator\\users.txt", "a")
            #print("Já existe arquivo")
            path = 2
        finally:
            name = dv.inputName("Inform user's name: ", "User's name")
            age = dv.inputInt("Inform user's age: ", "User's age")
            if path == 1:
                file.write(f"{name:<55}{age:>3} years old")
            else:
                file.write(f"\n{name:<55}{age:>3} years old")
            dv.texto("User registration complete!")
        print("-"*70)
        choice = dv.inputYN("Do you wish to register another user [Y/N]? ")
        if choice == "N":
            break