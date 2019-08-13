import modules.data as dv


def listUsers():
    try:
        file = open("G:\\Hans Documents\\dev\\User-Registrator\\users.txt", "r")
    except Exception:
        result = "There are no registered users to list."
    else:
        result = file.read()
        dv.titulo("Registered Users")
    return print(result)


listUsers()
