import sys
from functools import partial
from termcolor import colored

MENU = {
    1: "Registrar usuario",
    2: "Listar usuarios",
    3: "Iniciar sesión",
    4: "Salir",
}


DATA = dict()  # Keys: users; Values: passwords


def colored_print(text: str, color: str) -> None:
    """
        Prints text in console with color using termcolor library.

        Args:
        - text (str): Text to print in console.
        - color (str): Color for the text.

        Returns:
        - None
    """
    ctext = colored(text, color, attrs=["bold"])
    print(ctext)


# colored_print function wrappers
cprint_success = partial(colored_print, color="green")
cprint_warning = partial(colored_print, color="yellow")
cprint_failure = partial(colored_print, color="red")
cprint_info = partial(colored_print, color="blue")


def register(DB: dict) -> None:
    '''
        Register a user in the database.

        Args:
        - DB (dict): Dictionary where the user will be saved.

        Returns:
        - None
    '''
    try:
        user_name = input("Ingrese un nombre de usuario:\n").strip()
        if not user_name:
            cprint_failure("El nombre de usuario no puede estar vacío.")
            return

        if user_name in DB:
            cprint_warning(f"El usuario {user_name} ya está registrado.")
            return

        user_pass = input("Ingrese una contraseña:\n").strip()
        if not user_pass:
            cprint_failure("La contraseña no puede estar vacía.")
            return

        DB[user_name] = user_pass
        cprint_success(f"Usuario {user_name} registrado con éxito.")

    except KeyboardInterrupt:
        cprint_failure("Proceso de registro interrumpido por el usuario.")
    except Exception as e:
        cprint_failure(f"Ocurrión un error inesperado: {e}")


def print_data(DB: dict) -> None:
    """
        Prints DB data.

    Args:
    - DB (dict): Dictionary of users.

    Returns:
    - None
    """
    try:
        if not DB:
            cprint_warning("La base de datos no contiene usuarios.")
            return

        for user, password in DB.items():
            cprint_info(f"User: {user} | Password: {password}")
    except Exception as e:
        cprint_failure(f"Ocurrión un error inesperado: {e}")


def login(DB: dict) -> None:
    """
        Allows an user to login.

    Args:
    - DB (dict): Dictionary of users.

    Returns:
    - None
    """
    try:
        user_name = input("Ingrese el nombre de usuario:\n").strip()
        if not user_name:
            cprint_failure("El nombre de usuario no puede estar vacío.")
            return

        if user_name not in DB:
            cprint_warning(f"El usuario {user_name} no está registrado.")
            return

        user_pass = input("Ingrese la contraseña de usuario:\n")
        if DB[user_name] != user_pass:
            cprint_failure("Contraseña incorrecta.")
            return

        cprint_success("Inicio de sesión exitoso.")
    except KeyboardInterrupt:
        cprint_failure("Proceso de login interrumpido por el usuario.")
    except Exception as e:
        cprint_failure(f"Ocurrión un error inesperado: {e}")


def menu(menu: dict) -> None:
    """
        Prints a menu from a dict.

        Args:
        - menu (dict): Menu dict. Keys are the options and values are the descriptions.

        Returns:
        - None
    """
    try:
        if not menu:
            cprint_failure("Menú vacío.")
            return

        cprint_info("¿Qué desea hacer?")
        for option, description in menu.items():
            cprint_info(f"Opción {option} -> {description}")
    except Exception as e:
        cprint_failure(f"Ocurrión un error inesperado: {e}")


def get_menu_option(menu: dict) -> int:
    """
        Gets a menu option from the user.

        Args:
        - menu (dict): Menu dict.

        Returns:
        - option (int)
        - None if it fails.
    """
    try:
        option = int(input("Seleccione una opción: "))
        if option < 1 or option > len(menu):
            cprint_failure(
                "Opción inválida. Seleccione una de las opciones disponibles.")
            return
    except ValueError:
        cprint_failure("Opción inválida. Debe ingresar un número.")
    except KeyboardInterrupt:
        cprint_failure(
            "Seleccione la opción correspondiente para finalizar el programa.")
    except Exception as e:
        cprint_failure(f"Ocurrión un error inesperado: {e}")
    else:
        return option


def main() -> None:
    """
        Main program to register, show and login users.

        Args:
        - None

        Returns:
        - None
    """
    try:
        while True:
            menu(MENU)
            option = get_menu_option(MENU)
            if option == 1:
                register(DATA)
            elif option == 2:
                print_data(DATA)
            elif option == 3:
                login(DATA)
            elif option == 4:
                break
    except KeyboardInterrupt:
        cprint_failure("Proceso principal interrumpido por el usuario.")
    except Exception as e:
        cprint_failure(f"Ocurrión un error inesperado: {e}")
    else:
        cprint_success("Proceso principal terminado con éxito.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        cprint_failure("Uso incorrecto.")
        cprint_info(
            "Este programa no acepta argumentos de línea de comandos (flags / opciones).")
        exit()
    main()
