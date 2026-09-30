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
    def __init__(self, movie_name, total_seats, ticket_price):
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_seats = 0

    def book_ticket(self, num_tickets):
        seats_available = self.total_seats - self.booked_seats
        if num_tickets <= 0:
            print("Enter a valid no.\n")
        elif num_tickets > seats_available:
            print("Sorry, not enough seats available\n")
        else:
            self.booked_seats += num_tickets
            print(f"Your {self.booked_seats} of tickits are booked, enjoy your movie!\n")
            print(f"The total price of the tickets are {self.ticket_price * num_tickets}\n")

    def show_status(self):
        seats_available = self.total_seats - self.booked_seats
        print(f"The name of the movie is {self.movie_name}\n")
        print(f"Total seats available = {seats_available}\n")
        print(f"Ticket price is = {self.ticket_price}\n")

m1 = Movie("Kargil", 100, 200)
m1.show_status()
m1.book_ticket(200)
m1.show_status()