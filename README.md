# Simple Movie Ticket Booking System 🎬

A lightweight, console-based **Movie Ticket Booking System** built in Python with the following features:

- 5 rows × 10 seats (50 total seats)
- Visual seat map (`O` = available, `X` = booked)
- Tiered pricing based on row proximity to screen (front rows cost more)
- 20% student discount
- Beautiful printed ticket with unique Ticket ID
- All bookings automatically saved to `bookings.txt`
- View all current bookings

Perfect for learning OOP concepts, file handling, and building interactive CLI applications.

---

### Features

| Feature                  | Description                                      |
|--------------------------|--------------------------------------------------|
| Seat Layout              | 5 rows (A–E) × 10 seats each                     |
| Dynamic Pricing          | Row A: $150, B: $120, C: $100, D: $80, E: $60    |
| Student Discount         | 20% off with valid student status                |
| Unique Ticket ID         | Auto-generated as `TKT0001`, `TKT0002`, etc.     |
| Persistent Storage       | Bookings saved to `bookings.txt`                 |
| Real-time Seat Updates   | Instantly reflects booked seats on the map       |



---

# Project Structure (OOP Design)
1. Class: Seat

Represents a single seat in the theater.

row, col

is_booked

get_name() → Converts seat to human-readable format (A1, B3)

2. Class: Theater

Manages all seats and pricing.

A 2D list of Seat instances

Row-wise pricing

show_seats() → displays seat layout

book_seat() → marks seat as booked

3. Class: Booking

Stores booking information.

Generates ticket ID

Calculates discount (if student)

print_ticket() → prints formatted ticket

to_string() → used for file saving

4. Class: TicketSystem

Controls the whole system.

Displays menu

Manages bookings

Handles user input

Saves each booking to bookings.txt

# How to Run
Step 1: Clone the Repository
git clone https://github.com/your-username/movie-ticket-system.git
cd movie-ticket-system

# Sample Output (Ticket)
<img width="1110" height="778" alt="image" src="https://github.com/user-attachments/assets/de69eabd-58f3-4f8c-9399-3d0fdc359bbb" />
Concepts Used

Classes & Objects

Inheritance (optional expansion)

File Handling

List & Loop Operations

Console UI

Validation & Error Handling
