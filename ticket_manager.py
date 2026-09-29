from models import Ticket, Priority


class TicketManager:
    def __init__(self):
        self.tickets = []
        self.id = 0

    def create_ticket(self):
        self.id += 1
        title = input("Enter Ticket Title: ")
        description = input("Enter Ticket Description: ")
        assigned_to = input("Enter Assigned Personnel: ").upper()
        priority_input = input("Enter Priority: ").upper()

        try:
            priority = Priority(priority_input)
        except ValueError:
            print("INVALID PRIORITY")
            return

        ticket = Ticket(
            self.id,
            title,
            description,
            assigned_to,
            priority
        )

        self.tickets.append(ticket)

    def view_ticket(self):
        print("View Ticket")
        for ticket in self.tickets:
            print(ticket)

    def update_ticket(self):
        id_choice = int(input("Enter id: "))
        for ticket in self.tickets:
            if ticket.id == id_choice:
                new_assigned_to = input("Enter new assigned personnel: ").upper()
                new_status = input("Enter new status: ").upper()
                new_priority = input("Enter new priority: ").upper()

                ticket.assigned_to = new_assigned_to
                ticket.status = new_status
                ticket.priority = new_priority

                print("Ticket Updated")

        print("TICKET NOT FOUND")

    def remove_ticket(self):
        choice = int(input("Enter id: "))
        for ticket in self.tickets:
            if ticket.id == choice:
                self.tickets.remove(ticket)
                print(f"Ticket {ticket.id} removed")

        print("TICKET NOT FOUND")
