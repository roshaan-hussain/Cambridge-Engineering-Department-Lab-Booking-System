class User:
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return f"<User: {self.username} ({self.role})>"


class Lab:
    def __init__(self, lab_id, name, capacity):
        self.lab_id = lab_id
        self.name = name
        self.capacity = capacity

    def __repr__(self):
        return f"<Lab: {self.name}, Cap: {self.capacity}>"


class Booking:
    def __init__(self, booking_id, user, lab, date, time_slot):
        self.booking_id = booking_id
        self.user = user
        self.lab = lab
        self.date = date
        self.time_slot = time_slot

    def __repr__(self):
        return f"<Booking: {self.user.username} in Lab {self.lab.lab_id} on {self.date} from {self.time_slot}.>"


class BookingSystem:
    def __init__(self):
        self.users = []
        self.labs = []
        self.bookings = []

    def register_user(self, user):
        if user in self.users:
            print(f"{user.username} is already in the system.")
        else:
            self.users.append(user)
            print(f"{user.username} has been entered into the system.")

    def add_lab(self, lab):
        if lab in self.labs:
            print(f"Lab {lab.lab_id} is already in the system.")
        else:
            self.labs.append(lab)
            print(f"{lab.lab_id} has been entered into the system.")

    def create_booking(self, booking):
        for existing in self.bookings:
            if existing.lab == booking.lab and existing.date == booking.date and existing.time_slot == booking.time_slot:
                print(f"This lab is already booked at the specified date and time.")
                return
        self.bookings.append(booking)
        print(f"This booking has been entered into the system.")


user1 = User(947, "roshaan4", "123456", "Student")

lab1 = Lab(21, "Thermofluids", 30)

booking1 = Booking(21, user1, lab1,
                   "12/09/2026", "9-11")


system = BookingSystem()
system.register_user(user1)
system.add_lab(lab1)
system.create_booking(booking1)
system.create_booking(booking1)
