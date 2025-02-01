# function that generates a random password

from random import choice

def generate_password(length=12):
    """Genera una contraseña aleatoria de la longitud especificada."""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
    return "".join(choice(characters) for _ in range(length))

def write_passwords_to_file(filename, num_passwords):
    """Genera contraseñas aleatorias y las escribe en un archivo."""
    with open(filename, "w") as file:
        for _ in range(num_passwords):
            password = generate_password()
            file.write(f"{password}\n")

def main():
    # Generar contraseñas y escribirlas en un archivo
    write_passwords_to_file("passwords.txt", 2000)
    #extract random password from the file and write it to another file
    with open("passwords.txt", "r") as file:
        passwords = file.readlines()
    with open("password", "w") as file:
        file.write(choice(passwords))
if __name__ == "__main__":
    main()