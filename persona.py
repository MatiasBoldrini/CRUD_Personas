
class Persona:
    def __init__(self):
        self.personas = {}
        self.database_directory = (
            'valores.txt'
        )

    def add_Users(self):
       # Checking if the user is in the database and if it is not, it will add the user to the
       # database.
        if self.check_input() and not self.is_user_in_DB(self.dni):
            with open(self.database_directory, "a") as f:
                f.write(self.dni + " " + self.nombre + " " + self.apellido)
                f.write("\n")
            return True

    def check_input(self, dni='', nombre='', apellido=''):
        # Asking for the user to input a name, surname and dni.
        nombre = input("Ingrese un nombre: ")
        apellido = input("Ingrese apellido: ")
        if dni == '':
            dni = input("Ingrese dni: ")
        if not (apellido and nombre and dni.isnumeric()):
            raise Exception("INCORRECT DATA")
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        return True

    def refresh_Users(self):
        """
        It reads the database file and creates a dictionary of users
        """
        lines = []
        with open(self.database_directory, "r") as f:
            lines = f.readlines()
        for line in lines:
            atributos = line.split()
            self.personas[atributos[0]] = atributos

    def modify_Users(self, dni):
        """
        It opens the file, reads the lines, and then writes the lines back to the file, except for the
        line that contains the dni
        
        :param dni: The DNI of the user you want to modify
        :return: a boolean value.
        """
        if self.check_input(dni) and self.is_user_in_DB(dni):
            with open(self.database_directory, "r") as f:
                lines = f.readlines()
            with open(self.database_directory, "w") as f:
                for line in lines:
                    if dni not in line.strip("\n"):
                        f.write(line)
                    else:
                        f.write(dni + " " + self.nombre + " " + self.apellido)
                        f.write("\n")
            return True

    def delete_Users(self, dni):
        """
        It deletes a user from the database
        
        :param dni: The DNI of the user you want to delete
        :return: A boolean value.
        """
        if self.is_user_in_DB(dni):
            with open(self.database_directory, "r") as f:
                lines = f.readlines()
            with open(self.database_directory, "w") as f:
                for line in lines:
                    if dni not in line.strip("\n"):
                        f.write(line)
            return True
        return False

    def is_user_in_DB(self, dni):
        self.refresh_Users()
        return dni in self.personas.keys()

    def get_User_Attributes(self, dni):
        self.refresh_Users()
        return self.personas.get(dni)


