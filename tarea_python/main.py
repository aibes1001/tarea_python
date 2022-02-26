
from aircraft import Aircraft, Airbus, Boeing
from flight import Flight
#from pprint import pp, pprint

def make_flights():
    
    f1 = Flight(number = "BA117", aircraft = Aircraft(registration = "G-EUAH", model = "Airbus A319", num_rows = 22, num_seats_per_row=6))
    f2 = Flight(number = "AF92", aircraft = Boeing(registration = "F-GSPS", airline = "Emirates")) 
    f3 = Flight(number = "BA148", aircraft = Airbus(registration = "G-EUPT", variant = "A319-100")) 
    f1.allocate_passenger("22A", ("Jack", "Shephard", "85994003S"))
    f1.allocate_passenger("20A", ("Kate", "Austen", "12589756P"))
    f1.allocate_passenger("18E", ("James", "Ford", "56278665F"))
    f1.allocate_passenger("1C", ("John", "Locke", "10265448H"))
    f1.allocate_passenger("4D", ("Sayid", "Jarrah", "15758664M"))

    return f1, f2, f3
    

try:
    f1, f2, f3 = make_flights()
    
    for fl in f1, f2, f3:
        fl.print_seating()
        print('\n')
        fl.print_boarding_cards()
        print('\n')
    

    f1.reallocate_passenger("22A", "1A")

    f1.print_boarding_cards()

except Exception as e:
    print(type(e).__name__ + ": " + str(e))



