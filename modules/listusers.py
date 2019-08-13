import modules.data as dv


def listUsers():
    try:
        file = open("G:\\Hans Documents\\dev\\User-Registrator\\users.txt", "r")
    except Exception:
        print("-"*70)
        result = "\033[0;31mThere are no registered users to list.\033[m"
    else:
        result = file.read()
        dv.titulo("Registered Users")
        print(f"{'USER NAME                         ':^57}{'USERS AGE':^13}")
        print("-"*70)
    return print(result)
