from models import Ticket, Priority, Status
from ticket_repository import (
    ticket_exists,
    create_ticket,
    view_ticket,
    update_ticket,
    remove_ticket
)

class TicketManager:
    def create_ticket(self):
        title = input("Enter Ticket Title: ")
        description = input("Enter Ticket Description: ")
        assigned_to = input("Enter Assigned Personnel: ").upper()
        priority_input = input("Enter Priority: ").upper()

        try:
            priority = Priority(priority_input)
        except ValueError:
            print("INVALID PRIORITY !!!")
            return

        ticket = Ticket(
            None,
            title,
            description,
            assigned_to,
            priority
        )

        create_ticket(ticket)
        print(f"Ticket Created {ticket.id:03d} created")

    def view_ticket(self):
        view_option = int(input("""
        1 - View all tickets
        2 - Search for tickets
        """))
        if view_option == 1:
            id_choice = None
        elif view_option == 2:
            id_choice = int(input("Enter Ticket ID: "))

            if not ticket_exists(id_choice):
                print("TICKET NOT FOUND !!!")
                return
        else:
            print("INVALID SELECTION")
            return
        view_ticket(view_option, id_choice)

    def update_ticket(self):
        id_choice = int(input("Enter id: "))

        if not ticket_exists(id_choice):
            print("TICKET NOT FOUND !!!")
            return

        new_assigned_to = input("Enter new assigned personnel: ").upper()
        new_status = input("Enter new status: ").upper()
        try:
            status = Status(new_status)
        except ValueError:
            print("INVALID STATUS !!!")
            return
        new_priority = input("Enter new priority: ").upper()
        try:
            priority = Priority(new_priority)
        except ValueError:
            print("INVALID PRIORITY !!!")
            return
        update_ticket(id_choice, new_assigned_to, status, priority)

    def remove_ticket(self):
        id_choice = int(input("Enter id: "))

        if not ticket_exists(id_choice):
            print("TICKET NOT FOUND !!!")
            return

        remove_ticket(id_choice)
