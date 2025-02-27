from termcolor import colored


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


def cprint_success(text):
    """
        Prints text in green color. Wrapper for colored_print function.

        Args:
        - text (str): Text to print in console.

        Returns:
        - None
    """
    colored_print(text, "green")


def cprint_warning(text):
    """
        Prints text in yellow color. Wrapper for colored_print function.

        Args:
        - text (str): Text to print in console.

        Returns:
        - None
    """
    colored_print(text, "yellow")


def cprint_failure(text):
    """
        Prints text in red color. Wrapper for colored_print function.

        Args:
        - text (str): Text to print in console.

        Returns:
        - None
    """
    colored_print(text, "red")


def cprint_info(text):
    """
        Prints text in blue color. Wrapper for colored_print function.

        Args:
        - text (str): Text to print in console.

        Returns:
        - None
    """
    colored_print(text, "blue")


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

        user_pass = input("Ingrese una contraseña:\n").strip()
        if not user_pass:
            cprint_failure("La contraseña no puede estar vacía.")
            return

        if user_name not in DB:
            DB[user_name] = user_pass
            cprint_success(f"Usuario {user_name} registrado con éxito.")
        else:
            cprint_warning(f"El usuario {user_name} ya está registrado.")
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


def login(DB: dict):
    """
        Allows a user to login.

    Args:
    - DB (dict): Dictionary of users.

    Returns:
    - None
    """
    try:
        user_name = input("Ingrese el nombre de usuario:\n").strip()
        user_pass = input("Ingrese la contraseña de usuario:\n").strip()
    except Exception as e:
        cprint_failure(f"Ocurrión un error inesperado: {e}")


data = dict()  # Keys: user_name; Values: user_pass

register("")
print_data(data)
