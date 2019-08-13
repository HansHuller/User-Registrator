import modules.data as dv


def register():
    try:
        file = open("G:\\Hans Documents\\dev\\User-Registrator\\users.txt")
    except Exception:
        file = open("G:\\Hans Documents\\dev\\User-Registrator\\users.txt", "w")
        print("Arquivo Criado")
    else:
        print("Já existe arquivo")


register()