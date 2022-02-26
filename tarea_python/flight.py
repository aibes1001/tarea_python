


class Flight:

    """
    Clase Flight
    """

    def __init__(self, number, aircraft):
        """
        Inicializa un vuelo con información del número del vuelo y el tipo de avión

        Args:
            number (string): Texto con el id del vuelo
            aircraft (object): Objeto de la clase Aircraft con la información del avión

        Raises:
            ValueError: Error que indica que el formato de las letras del vuelo no es correcto
            ValueError: Error que indica que el formato del número de vuelo no es correcto

        """
        for i in range(2):
            if number[i] < 'A' or number[i] > 'Z':
                raise ValueError("El formato de las letras del vuelo no es correcto")
         
        if number[2:].isdigit() and int(number[2:]) < 9999:
            self.__number = number
        else:
            raise ValueError("El formato del número vuelo no es correcto") 

        
        self.__aircraft = aircraft
        self.__seating = []

        #Configurem les files (es len + 1 perquè va de la fila 1 a la fila final que coincidix amb la len)
        for i in range(len(self.__aircraft.seating_plan()[0]) + 1):

            if i != 0:
                self.__seating.insert(i,{})
                #Configurem els seients per cada fila
                for j in self.__aircraft.seating_plan()[1]:
                    self.__seating[i].update({j: None})
            else:
                #Inserta en la posició 0 un None
                self.__seating.insert(i,None)
        
        #print("Asientos", len(self.__seating)-1)
            
        


    def __parse_seat(self, seat):
        """ 
        Método privado para separar el número de fila y la posición (letra) de un asiento

        Args:
            seat (string): Texto con la fila y la letra del asiento

        Raises:
            ValueError: _description_
            ValueError: _description_

        Returns:
            row (int): Número de fila del asiento
            letter (string): Letra del asiento
        """
        row = seat[:len(seat) - 1]
        letter = seat[-1]
        for i in range (len(row)):
            if row[i] < '0' or row[i] > '9':
                raise ValueError("El formato del asiento no es correcto")
        
        if int(row) <= len(self.__aircraft.seating_plan()[0]) and int(row) > 0 and letter <= self.__aircraft.seating_plan()[1][-1]:
            return  int(row), letter
        else:
            raise ValueError("El formato del asiento no es correcto")   


    def __passenger_seats(self):
        """
        Método privado para obtener la información de los pasajeros que están asignados a los asientos

        Yields:
            tupla: Tupla con la información de los pasajeros, y el número de fila y letra del asiento
        """
        for i in range(1, len(self.__aircraft.seating_plan()[0]) + 1):
            for j in self.__aircraft.seating_plan()[1]:
                if self.__seating[i][j] != None:
                    yield (self.__seating[i][j], str(i) + j)

    
    def allocate_passenger(self, seat, passenger):
        """
        Método para alojar un pasajero a un asiento

        Args:
            seat (string): texto que contiene el número de la fila y la letra del asiento
            passenger (object): objeto de la clase Passenger con la información de un pasajero

        Raises:
            ValueError: Error que indica que el asiento ya está asignado a un pasajero
        """
        row, letter = self.__parse_seat(seat)

        if self.__seating[row][letter] == None:
            self.__seating[row].update({letter : passenger})
        else:
            raise ValueError("El asiento " + seat + " ya está ocupado") 

 
    def reallocate_passenger(self, from_seat, to_seat):
        """
        Método para realojar a un pasajero a un nuevo asiento

        Args:
            from_seat (string): Texto con la información del asiento de origen
            to_seat (string): Texto con la información del asiento de destino

        Raises:
            ValueError: Error que indica que el asiento de origen no está ocupado por ningún pasajero
        """
        origin_row, origin_letter = self.__parse_seat(from_seat)

        if self.__seating[int(origin_row)][origin_letter] == None:
            raise ValueError("El asiento " + from_seat + " aún está vacío")
        else:
            passenger = self.__seating[int(origin_row)].get(origin_letter)
            self.allocate_passenger(to_seat, passenger)
    

    def num_available_seats(self):
        """
        Método que cuenta el número de asientos disponibles en el vuelo

        Returns:
            count (int): Número de asientos disponibles
        """
        count = 0

        for i in range(1, len(self.__seating)):
            for key in self.__seating[i]:
                if self.__seating[i][key] == None:
                    count += 1

        return count
    

    def print_seating(self):
        """
        Método que imprime todos los asientos ordenados por filas de un vuelo
        """
        for i in range(1, len(self.__seating)):
            print(str(i) + " " + str(self.__seating[i]))

    
    def print_boarding_cards(self):
        """
        Método que imprime la información de la tarjeta de embarque de los pasajeros
        """
        generador = self.__passenger_seats()

        for i in generador:
            print(i[0][0], i[0][1], i[0][2], i[1], self.__number, self.__aircraft.get_model())








    
