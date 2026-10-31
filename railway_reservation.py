class RailwayReservation:
    def __init__(self):
        self.trains = {
            1: {"name": "Express", "seats": 5},
            2: {"name": "Superfast", "seats": 3},
            3: {"name": "Local", "seats": 10}
        }
        self.bookings = {}

    def view_trains(self):
        print("Available Trains:")
        for train_id, details in self.trains.items():
            print(f"Train ID: {train_id}, Name: {details['name']}, Seats: {details['seats']}")

    def book_ticket(self, name, train_id):
        if train_id in self.trains and self.trains[train_id]["seats"] > 0:
            self.trains[train_id]["seats"] -= 1
            self.bookings[name] = train_id
            print("Ticket booked successfully!")
        else:
            print("No seats available or invalid train.")

    def cancel_ticket(self, name):
        if name in self.bookings:
            train_id = self.bookings[name]
            self.trains[train_id]["seats"] += 1
            del self.bookings[name]
            print("Ticket cancelled successfully!")
        else:
            print("No booking found.")

# Main Program
system = RailwayReservation()

while True:
    print("\n1. View Trains\n2. Book Ticket\n3. Cancel Ticket\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        system.view_trains()
    elif choice == 2:
        name = input("Enter your name: ")
        train_id = int(input("Enter train ID: "))
        system.book_ticket(name, train_id)
    elif choice == 3:
        name = input("Enter your name: ")
        system.cancel_ticket(name)
    elif choice == 4:
        break
    else:
        print("Invalid choice")
