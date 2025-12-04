# Simple Movie Ticket Booking System

class Seat:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.is_booked = False
    
    def get_name(self):
        return f"{chr(65 + self.row)}{self.col + 1}"  # A1, A2, B1, etc.


class Theater:
    def __init__(self):
        # 5 rows × 10 seats (2D list)
        self.seats = [[Seat(r, c) for c in range(10)] for r in range(5)]
        
        # Front rows cost more
        self.prices = {
            0: 150,  # Row A - Front (expensive)
            1: 120,  # Row B
            2: 100,  # Row C
            3: 80,   # Row D
            4: 60    # Row E - Back (cheapest)
        }
    
    def show_seats(self):
        print("\n        SCREEN")
        print("  " + "-" * 32)
        print("    1  2  3  4  5  6  7  8  9  10")
        
        for r in range(5):
            row_letter = chr(65 + r)
            print(f"{row_letter}  ", end="")
            for c in range(10):
                if self.seats[r][c].is_booked:
                    print(" X ", end="")
                else:
                    print(" O ", end="")
            print(f"  ${self.prices[r]}")
        
        print("\nO = Available, X = Booked")
    
    def book_seat(self, row, col, name):
        self.seats[row][col].is_booked = True


class Booking:
    booking_count = 0
    
    def __init__(self, name, seat, price, is_student, movie):
        Booking.booking_count += 1
        self.id = f"TKT{Booking.booking_count:04d}"
        self.name = name
        self.seat = seat
        self.is_student = is_student
        self.movie = movie
        
        # Calculate price with student discount (20%)
        if is_student:
            self.discount = price * 0.20
            self.total = price - self.discount
        else:
            self.discount = 0
            self.total = price
    
    def print_ticket(self):
        print("\n" + "=" * 40)
        print("   MOVIE TICKET ")
        print("=" * 40)
        print(f"  Ticket ID  : {self.id}")
        print(f"  Movie      : {self.movie}")
        print(f"  Name       : {self.name}")
        print(f"  Seat       : {self.seat.get_name()}")
        print(f"  Student    : {'Yes' if self.is_student else 'No'}")
        print(f"  Discount   : ${self.discount:.2f}")
        print(f"  Total      : ${self.total:.2f}")
        print("=" * 40)
        print("     Enjoy your movie! 🍿")
        print("=" * 40)
    
    def to_string(self):
        return f"{self.id},{self.name},{self.seat.get_name()},{self.total},{self.movie}\n"


class TicketSystem:
    def __init__(self):
        self.theater = Theater()
        self.bookings = []
        self.movie = "Avengers: Endgame"
        self.filename = "bookings.txt"
    
    def save_to_file(self, booking):
        with open(self.filename, "a") as f:
            f.write(booking.to_string())
        print(f"Saved to {self.filename}")
    
    def book_ticket(self):
        self.theater.show_seats()
        
        # Get customer info
        name = input("\nEnter your name: ")
        
        # Get row (A-E)
        row_input = input("Enter row (A-E): ").upper()
        if row_input not in "ABCDE":
            print("Invalid row!")
            return
        row = ord(row_input) - 65
        
        # Get seat number (1-10)
        try:
            col = int(input("Enter seat (1-10): ")) - 1
            if col < 0 or col > 9:
                print("Invalid seat!")
                return
        except:
            print("Invalid input!")
            return
        
        # Check if available
        if self.theater.seats[row][col].is_booked:
            print("Seat already booked!")
            return
        
        # Student discount
        is_student = input("Are you a student? (y/n): ").lower() == 'y'
        
        # Get price and create booking
        price = self.theater.prices[row]
        seat = self.theater.seats[row][col]
        
        booking = Booking(name, seat, price, is_student, self.movie)
        
        # Book the seat
        self.theater.book_seat(row, col, name)
        self.bookings.append(booking)
        
        # Print ticket and save
        booking.print_ticket()
        self.save_to_file(booking)
    
    def view_bookings(self):
        print("\n" + "=" * 50)
        print("ALL BOOKINGS")
        print("=" * 50)
        
        if not self.bookings:
            print("No bookings yet!")
            return
        
        print(f"{'ID':<10} {'Name':<15} {'Seat':<6} {'Total':<8}")
        print("-" * 50)
        for b in self.bookings:
            print(f"{b.id:<10} {b.name:<15} {b.seat.get_name():<6} ${b.total:<.2f}")
    
    def run(self):
        while True:
            print(f"\n=== MOVIE: {self.movie} ===")
            print("1. View Seats")
            print("2. Book Ticket")
            print("3. View Bookings")
            print("4. Exit")
            
            choice = input("Choose (1-4): ")
            
            if choice == "1":
                self.theater.show_seats()
            elif choice == "2":
                self.book_ticket()
            elif choice == "3":
                self.view_bookings()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")


# Run the program
if __name__ == "__main__":
    system = TicketSystem()
    system.run()