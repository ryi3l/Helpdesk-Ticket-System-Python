from models import Ticket, Priority, Status
from exceptions import DatabaseError
from ticket_repository import (
    ticket_exists,
    create_ticket,
    get_all_tickets,
    get_ticket_by_id,
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

        try:
            create_ticket(ticket)
            print(f"Ticket Created {ticket.id:03d} created")
        except DatabaseError:
            print("DATABASE ERROR: Unable to create ticket.")

    def view_ticket(self):
        try:
            view_option = int(input("""
            1 - View all tickets
            2 - Search for tickets
            Answer: 
            """))
        except ValueError:
            print("INVALID OPTION !!!")
            return
        if view_option == 1:
            try:
                results = get_all_tickets()
            except DatabaseError:
                print("DATABASE ERROR: Unable to get all tickets.")
                return
        elif view_option == 2:
            try:
                id_choice = int(input("Enter Ticket ID: "))
            except ValueError:
                print("INVALID TICKET ID !!!")
                return
            try:
                if not ticket_exists(id_choice):
                    print("TICKET NOT FOUND !!!")
                    return
            except DatabaseError:
                print("DATABASE ERROR: Unable to check if ticket exists.")
                return
            try:
                result = get_ticket_by_id(id_choice)
                results = [result]
            except DatabaseError:
                print("DATABASE ERROR: Unable to get ticket by ID.")
                return
        else:
            print("INVALID SELECTION")
            return

        for row in results:
            print(row)

    def update_ticket(self):
        try:
            id_choice = int(input("Enter Ticket ID: "))
        except ValueError:
            print("INVALID TICKET ID !!!")
            return
        try:
            if not ticket_exists(id_choice):
                print("TICKET NOT FOUND !!!")
                return
        except DatabaseError:
            print("DATABASE ERROR: Unable to check if ticket exists.")
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
        try:
            update_ticket(id_choice, new_assigned_to, status, priority)
            print("UPDATE SUCCESSFUL!")
        except DatabaseError:
            print("DATABASE ERROR: Unable to update ticket.")

    def remove_ticket(self):
        try:
            id_choice = int(input("Enter Ticket ID: "))
        except ValueError:
            print("INVALID TICKET ID !!!")
            return
        try:
            if not ticket_exists(id_choice):
                print("TICKET NOT FOUND !!!")
                return
        except DatabaseError:
            print("DATABASE ERROR: Unable to check if ticket exists.")
            return
        try:
            remove_ticket(id_choice)
            print("REMOVE SUCCESSFUL!")
        except DatabaseError:
            print("DATABASE ERROR: Unable to remove ticket.")
