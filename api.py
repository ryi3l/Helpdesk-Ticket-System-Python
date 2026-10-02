from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import Priority, Ticket, Status
from ticket_repository import (get_all_tickets,
                               get_ticket_by_id,
                               remove_ticket,
                               create_ticket,
                               update_ticket,
                               ticket_exists
                               )

app = FastAPI()

class TicketCreate(BaseModel):
    title: str
    description: str
    assigned_to: str
    priority: Priority

class TicketUpdate(BaseModel):
    assigned_to: str
    status: Status
    priority: Priority

@app.get("/tickets")
def get_tickets():
    return get_all_tickets()

@app.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int):
    result = get_ticket_by_id(ticket_id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )
    return result

@app.post("/tickets", status_code = 201)
def create_ticket_endpoint(ticket_data: TicketCreate):
    ticket = Ticket(
        None,
        title=ticket_data.title,
        description=ticket_data.description,
        assigned_to=ticket_data.assigned_to,
        priority=ticket_data.priority
    )
    create_ticket(ticket)
    return ticket

@app.put("/tickets/{ticket_id}")
def update_ticket_endpoint(ticket_id: int, ticket_data: TicketUpdate):
    if not ticket_exists(ticket_id):
        raise HTTPException(status_code=404, detail="Ticket not found")
    update_ticket(
        ticket_id,
        ticket_data.assigned_to,
        ticket_data.status,
        ticket_data.priority
    )
    return ticket_data

@app.delete("/tickets/{ticket_id}")
def delete_ticket_endpoint(ticket_id: int):
    if not ticket_exists(ticket_id):
        raise HTTPException(status_code=404, detail="Ticket not found")
    remove_ticket(ticket_id)
    return {"message": "Ticket deleted"}