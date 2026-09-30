from database import get_connection

def create_ticket(ticket):
    connection = get_connection()
    cursor = connection.cursor()

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

    cursor.close()
    connection.close()

def view_ticket(view_option, id_choice):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    if view_option == 1:
        query = """
            SELECT * FROM tickets;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    elif view_option == 2:
        query = """
            SELECT * FROM tickets WHERE id = %s;
        """
        values = (id_choice,)
        cursor.execute(query, values)
        results = cursor.fetchall()
        for row in results:
            print(row)

    cursor.close()
    connection.close()

def update_ticket(id_choice, new_assigned_to, status, priority):
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        UPDATE tickets
        SET assigned_to = %s, status = %s, priority = %s
        WHERE id = %s;
    """
    values = (new_assigned_to, status.value, priority.value, id_choice)
    cursor.execute(query, values)
    connection.commit()
    print("UPDATE SUCCESSFUL!")

    cursor.close()
    connection.close()

def remove_ticket(id_choice):
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        DELETE FROM tickets
        WHERE id = %s;
    """
    values = (id_choice,)
    cursor.execute(query, values)
    connection.commit()
    print("REMOVE SUCCESSFUL!")

    cursor.close()
    connection.close()

def ticket_exists(ticket_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT id FROM tickets
        WHERE id = %s;
    """

    cursor.execute(query, (ticket_id,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result is not None