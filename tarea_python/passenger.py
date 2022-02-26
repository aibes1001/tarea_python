


class Passenger:

    """
    Clase Passenger
    """

    def __init__(self, name, surname, id_card):
        """
        Inicializador de un pasajero con su nombre, apellido y id

        Args:
            name (string): Texto con el nombre del pasagero
            surname (string): Texto con el apellido
            id_card (string): Texto con el id
        """
        self.__name = name
        self.__surname = surname
        self.__id_card = id_card

    def passenger_data(self):
        """
        Método que devuelve la información del pasagero

        Returns:
            tupla: tupla con el nombre, apellido e id
        """
        return (self.__name, self.__surname, self.__id_card)

