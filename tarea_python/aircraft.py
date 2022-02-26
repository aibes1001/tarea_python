


class Aircraft:

    """
    Clase Aircraft
    """

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        """
        Inicializador de la clase aircraft

        Args:
            registration (str): Texto con el registro del avión 
            model (str): Texto con la información del tipo de avión
            num_rows (int): Número de filas que tiene
            num_seats_per_row (int): _description_
        """
        self.__registration = registration
        self.__model = model
        self.__num_rows = num_rows
        self.__num_seats_per_row = num_seats_per_row
    

    def get_registration(self):
        return self.__registration
    

    def get_model(self):
        return self.__model
    

    def seating_plan(self):
        """
        Método que devuelve el número de filas y los asientos por fila del avión

        Returns:
            tupla: Número entero con las filas, y texto con la concatenación de las letras de cada asiento por fila
        """

        list_rows = []
        for i in range(self.__num_rows):
            if i == 0:
                list_rows.insert(i,None)
            else:
                list_rows.insert(i, i)

        #list_rows = [i + 1 for i in range(self.__num_rows)]

        #Per a la nomenclatura dels seients de cada fila convertirem de ASCII a caracter i concatenem
        str_seats_per_row = ""
        for i in range(self.__num_seats_per_row):
            str_seats_per_row += chr(i+65)

        return (list_rows, str_seats_per_row)
    

    def num_seats(self):
        """
        Método que devuelve el número de asientos que tiene el avión

        Returns:
            int: Número de asientos
        """
        return self.__num_seats_per_row * self.__num_rows
    
    



class Airbus(Aircraft):

    """
    Clase Boeing que hereda da la clase Aircraft
    """

    __model = "Airbus A319"
    __num_rows = 23
    __num_seats_per_row = 6

    def __init__(self, registration, variant):
        """
        Inicializador de un avión de tipo Airbus A319

        Args:
            registration (str): Texto con el registro del avión 
            variant (str): Texto con la variante del modelo
        """
        super().__init__(registration, self.__model, self.__num_rows, self.__num_seats_per_row)
        self.__variant = variant
    
    def get_variant(self):
        return self.__variant





class Boeing(Aircraft):

    """
    Clase Boeing que hereda da la clase Aircraft

    """

    __model = "Boeing 777"
    __num_rows = 56
    __num_seats_per_row = 9

    def __init__(self, registration, airline):
        """
        Inicializador de un avión de tipo Boeing 777

        Args:
            registration (str): Texto con el registro del avión 
            airline (str): Texto con la información de la aerolínia que opera
        """
        super().__init__(registration, self.__model, self.__num_rows, self.__num_seats_per_row)
        self.__airline = airline
    
    def get_airline(self):
        return self.__airline
    

