import mysql.connector
from database import get_connection
from exceptions import DatabaseError

def create_ticket(ticket):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                query = """
                    INSERT INTO tickets(
                        title,
                        description,
                        assigned_to,
                        status,
                        priority
                    )
                    VALUES (%s, %s, %s, %s, %s);
                """
                values = (
                    ticket.title,
                    ticket.description,
                    ticket.assigned_to,
                    ticket.status.value,
                    ticket.priority.value
                )

                cursor.execute(query, values)
                connection.commit()
                ticket.id = cursor.lastrowid
    except mysql.connector.Error as e:
        raise DatabaseError("Failed to create ticket.") from e

def get_all_tickets():
    try:
        with get_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:

                query = """
                    SELECT * FROM tickets;
                """
                cursor.execute(query)
                results = cursor.fetchall()
                return results
    except mysql.connector.Error as e:
        raise DatabaseError("Failed to get all tickets.") from e

def get_ticket_by_id(id_choice):
    try:
        with get_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                query = """
                        SELECT * FROM tickets
                        WHERE id = %s;
                """
                cursor.execute(query, (id_choice,))
                results = cursor.fetchone()
                return results
    except mysql.connector.Error as e:
        raise DatabaseError("Failed to get ticket.") from e

def update_ticket(id_choice, new_assigned_to, status, priority):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                query = """
                    UPDATE tickets
                    SET assigned_to = %s, status = %s, priority = %s
                    WHERE id = %s;
                """
                values = (new_assigned_to, status.value, priority.value, id_choice)
                cursor.execute(query, values)
                connection.commit()
    except mysql.connector.Error as e:
        raise DatabaseError("Failed to update ticket.") from e

def remove_ticket(id_choice):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                query = """
                    DELETE FROM tickets
                    WHERE id = %s;
                """
                values = (id_choice,)
                cursor.execute(query, values)
                connection.commit()
    except mysql.connector.Error as e:
        raise DatabaseError("Failed to remove ticket.") from e

def ticket_exists(ticket_id):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                query = """
                SELECT id FROM tickets
                    WHERE id = %s;
                """
                cursor.execute(query, (ticket_id,))
                result = cursor.fetchone()
                return result is not None
    except mysql.connector.Error as e:
        raise DatabaseError("Failed to check if ticket exists.") from e