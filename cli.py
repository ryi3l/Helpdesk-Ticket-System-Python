from ticket_manager import TicketManager
def menu():
    ticket_manager = TicketManager()
    while True:
        print("""
        1 - Create Ticket
        2 - View Tickets
        3 - Update Ticket
        4 - Remove Ticket
        5 - Exit
        """)

        choice = input("What do you want to do?: ")

        match choice:
            case "1":
                ticket_manager.create_ticket()
            case "2":
                ticket_manager.view_ticket()
            case "3":
                ticket_manager.update_ticket()
            case "4":
                ticket_manager.remove_ticket()
            case "5":
                print("bye bye")
                break
            case _:
                print("INVALID INPUT")