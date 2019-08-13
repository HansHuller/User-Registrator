def titulo(frase):
    print("-" * 70)
    print(f"{frase.upper():^70}")
    print("-" * 70)


def texto(frase):
    print(f"{frase.upper():<40}")


def choose(text="\033[33mWhat's your choice?\033[m ", errormsg="Invalid option! Try Again!"):
    choice = " "
    while not isinstance(choice, int):
        choice = input(f"{text:<40}")
        try:
            choice = int(choice)
        except:
            print("-"*70)
            print(f"{errormsg}")
            print("-"*70)
        else:
            if not (0 < choice < 4):
                choice = " "
                print("-" * 70)
                print(f"{errormsg}")
                print("-" * 70)
    return choice


def inputInt(frase = "Inform an integer number: ", nomeVar = "Variable"):
    aux = " "
    while not isinstance(aux, int):
        aux = input(f"{frase:<30}")
        if aux == "":
            aux = 0
        try:
            aux = int(aux)
        except ValueError:
            print(f"\033[1;31m{nomeVar.upper()}\033[m \033[0;31mMust be integer! Try again...\033[m")
    return aux


def inputFloat(frase = "Inform a float number: ", nomeVar = "Variable"):
    aux = " "
    while not isinstance(aux, float):
        aux = input(f"{frase:<30}").replace(",", ".")
        if aux == "":
            aux = 0
        try:
            aux = float(aux)
        except ValueError:
            print(f"\033[1;31m{nomeVar.upper()}\033[m \033[0;31mMust be float! Try again...\033[m")
    return aux


def inputStr(text = "Inform a text: ", varName = "Variable"):
    aux = 0
    while not isinstance(aux, str):
        aux = input(f"{text:<30}")
        if aux == "":
            aux = 0
        try:
                aux = float(aux)
                aux = int(aux)
                print(f"\033[1;31m{varName.upper()}\033[m \033[0;31mmust be a text! Try again...\033[m")
        except ValueError:
            aux = str(aux)
    return aux


def inputName(text = "Inform a name: ", varName = "Name"):
    aux = 0
    while not isinstance(aux, str):
        aux = input(f"{text:<30}")
        if aux == "":
            aux = 0
        count = 0
        for letter in aux:
            if letter in "0123456789/*-+.,´~[]/;?:}^{`=_!@#$%¨&*()":
                count += 1
        if count >0:
            aux = 0
        try:
                aux = float(aux)
                aux = int(aux)
                print(f"\033[1;31m{varName.upper()}\033[m \033[0;31mmust be a text! Try again...\033[m")
        except ValueError:
            aux = str(aux)
    return aux


def inputYN(text = "Do you which to continue [Y/N]? "):
    aux = 0
    while str(aux) not in "YN":
        aux = input(f"{text:<30}").upper()
        if aux not in "YN":
            print(f"Invalid option! Try Again!")
    return aux
