class movie :
    def __init__(self,movie_name:str,total_seats:int,ticket_price:int):
        self.movie_name = movie_name 
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_seats = 0 

    def book_tickets(self,num_of_tickets):
        if num_of_tickets > self.total_seats - self.booked_seats :
            print("Sorry , Not enough seats are available")
        else:
            self.booked_seats+= num_of_tickets
            self.total_seats-=num_of_tickets
            print(f"Your tickets are booked")
            print(f"Total Price = {self.ticket_price * num_of_tickets}\n")



    def show_status(self):
        # seats_available = self.total_seats -  self.booked_seats #Here is no need to write self.seats_available because this variable is only for this func method 
        print(f"Movie name  = {self.movie_name}" )
        print(f"Seats available  = {self.total_seats}")
        print(f"Total booked  = { self.booked_seats}")


Movie=movie("Krish",300,250)

Movie.book_tickets(150)
Movie.show_status()