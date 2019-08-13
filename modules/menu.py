import modules.data as dv
import modules.register as rg
import modules.listusers as lu


def menu():
    while True:
        dv.titulo("Main menu")
        print("\033[33m1 - \033[m\033[34mList records\033[m")
        print("\033[33m2 - \033[m\033[34mRegister new user\033[m")
        print("\033[33m3 - \033[m\033[34mQuit\033[m")
        print("-" * 70)
        choice = dv.choose()
        if choice == 1:
            lu.listUsers()
        elif choice == 2:
            rg.register()
        else:
            break
    dv.titulo("Thanks for using our software! Have a good one!")
