"""
Create a class Movie with the following:

Attributes:
movie_name > name of the movie
total_seats -> total seats available in the theatre
ticket_price -> price per ticket
booked_seats -> starts at 0

Methods:
book_ticket(num_tickets) - books the given number of tickets. If enough seats are available,
confirm the booking and show the total amount to pay. If not,
show "Sorry, not enough seats available"

show_status() - displays movie name, seats available, and seats booked so far
"""


class Movie:
    def __init__(self, movie_name: str, total_seats: int, ticket_price: int) -> None:
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_seats = 0

    def book_ticket(self, num_tickets: int) -> None:
        seat_available = self.total_seats - self.booked_seats

        if num_tickets <= 0:
            print("Please enter a valid number of tickets\n")
        elif num_tickets > seat_available:
            print("Sorry, not enough seats available\n")
        else:
            self.booked_seats += num_tickets
            print("Your ticket is booked\n")
            print(f"Total price is {self.ticket_price * num_tickets}")

    def show_status(self) -> None:
        seat_available = self.total_seats - self.booked_seats
        print(f"The name of the movie is {self.movie_name}")
        print(f"The seats available for the movie is {seat_available}")
        print(f"The seats booked so far for the movie is {self.booked_seats}\n")

m1 = Movie("Kargil", 100, 499)

m1.show_status()
m1.book_ticket(70)
m1.show_status()