class Seat:
    def __init__(self, seat_number, row_number, seat_type):
        self.seat_number = seat_number
        self.row_number = row_number
        self.seat_type = seat_type
        self.reserved = False
        self.next = None

class FlightBookingSystem:
    def __init__(self, rows, cols):
        self.head = None
        self.rows = rows
        self.cols = cols
        self.initialize_seats()

    def initialize_seats(self):
        seat_types = ['window', 'middle', 'aisle', 'aisle', 'middle', 'window'] #* (self.cols // 3)
        for row in range(self.rows):
            for seat_in_row in range(self.cols):
                seat_number = row * self.cols + (seat_in_row + 1)
                new_seat = Seat(seat_number, row + 1, seat_types[seat_in_row])
                if not self.head:
                    self.head = new_seat
                else:
                    current = self.head
                    while current.next:
                        current = current.next
                    current.next = new_seat

    def check_availability(self, row_number=None, seat_type=None):
        available_seats = []
        current = self.head
        while current:
            if not current.reserved and (row_number is None or current.row_number == row_number) and (seat_type is None or current.seat_type == seat_type):
                available_seats.append((current.seat_number, current.row_number, current.seat_type))
            current = current.next
        return available_seats

    def reserve_seat(self, seat_number):
        current = self.head
        while current:
            if current.seat_number == seat_number:
                if not current.reserved:
                    current.reserved = True
                    print(f"Seat {seat_number} reserved.")
                    return 1
                else:
                    print(f"Seat {seat_number} is occupied.")
                    return 0
            current = current.next
        print(f"Seat {seat_number} not found.")
        return 0

    def suggest_optimal_seat(self, row_number=None, seat_type=None):
        current = self.head
        while current:
            if not current.reserved and (row_number is None or current.row_number == row_number) and (seat_type is None or current.seat_type == seat_type):
                return (current.seat_number, current.row_number, current.seat_type)
            current = current.next
        return "No available seats."

    def update_waiting_list(self, seat_number):
        # Assuming a simple list for waiting list
        waiting_list = []
        if len(waiting_list) <= int(0.05*r*c):
            waiting_list.append(seat_number)
            return f"Seat {seat_number} added to waiting list."
        return f"Waiting list is full."

    def cancel_reservation(self, seat_number):
        current = self.head
        while current:
            if current.seat_number == seat_number:
                if current.reserved:
                    current.reserved = False
                    return f"Reservation for seat {seat_number} cancelled."
                else:
                    return f"Seat {seat_number} is not reserved."
            current = current.next
        return f"Seat {seat_number} not found."

    def change_reservation(self, old_seat_number, new_seat_number):
        cancel_result = self.cancel_reservation(old_seat_number)
        if "cancelled successfully" in cancel_result:
            reserve_result = self.reserve_seat(new_seat_number)
            return reserve_result
        else:
            return cancel_result

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
flight_system = FlightBookingSystem(r, c)


choice = input("Enter choice: \n1)Book \n2)Cancel \n3)Change:\n")
if choice == "1":  
    print("Available seats:", flight_system.check_availability())
    seat_row_inp = int(input("Enter row number: "))
    seat_col_inp = input("Enter column preference(W/M/A): ").upper()
    seat_num1 = 0
    seat_num2 = 0
    if seat_col_inp == "W":
        seat_num1 = (seat_row_inp-1) * c + 1
        seat_num2 = (seat_row_inp-1) * c + 6
    elif seat_col_inp == "M":
        seat_num1 = (seat_row_inp-1) * c + 2
        seat_num2 = (seat_row_inp-1) * c + 5
    elif seat_col_inp == "A":
        seat_num1 = (seat_row_inp-1) * c + 3
        seat_num2 = (seat_row_inp-1) * c + 4
    else:
        print("Invalid input.")
        exit()
    if flight_system.reserve_seat(seat_num1):
        pass
    elif flight_system.reserve_seat(seat_num2):
        pass
    else:
        print("No available seats.")
        exit()
    print("Available seats:", flight_system.check_availability())
    print(flight_system.suggest_optimal_seat(seat_row_inp, seat_col_inp))
    print(flight_system.update_waiting_list(seat_num1))
    print(flight_system.cancel_reservation(seat_num1))
    print("Available seats:", flight_system.check_availability())
    print(flight_system.reserve_seat(seat_num2))
    print("Available seats:", flight_system.check_availability())
    print(flight_system.suggest_optimal_seat(seat_row_inp, seat_col_inp))
    print(flight_system.update_waiting_list(seat_num1))
    print(flight_system.cancel_reservation(seat_num1))
    print("Available seats:", flight_system.check_availability())


    # print(flight_system.reserve_seat(seat_num1))
    # print("Available seats:", flight_system.check_availability())
    # print(flight_system.suggest_optimal_seat(seat_row_inp, seat_col_inp))
    # print(flight_system.update_waiting_list(seat_num1))
    # print(flight_system.cancel_reservation(seat_num1))
    # print(flight_system.reserve_seat(5))
    # print("Available seats:", flight_system.check_availability())
    # print(flight_system.suggest_optimal_seat())
    # print(flight_system.update_waiting_list(11))
    # print(flight_system.reserve_seat(5))
    # print(flight_system.cancel_reservation(5))
    # print("Available seats:", flight_system.check_availability())
    # print(flight_system.change_reservation(4, 6))
    # print("Available seats:", flight_system.check_availability())
