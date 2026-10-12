const refreshButton = document.querySelector("#refresh-button");
const ticketsContainer = document.querySelector("#tickets-container");
const createTicketForm = document.querySelector("#create-ticket-form");
const titleInput = document.querySelector("#title");
const descriptionInput = document.querySelector("#description");
const assignedToInput = document.querySelector("#assigned-to");
const priorityInput = document.querySelector("#priority");
const updateButton = document.querySelector("#update-button");
const removeButton = document.querySelector("#remove-button");
const updateTicketContainer = document.querySelector("#update-ticket-container");
const removeTicketContainer = document.querySelector("#remove-ticket-container");
const notificationContainer = document.querySelector("#notification-container");



refreshButton.addEventListener("click", function() {
    ticketsContainer.textContent = "";
    fetch("http://127.0.0.1:8000/tickets")
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            data.forEach(function(ticket) {
                const div = document.createElement("div")
                div.classList.add("ticket");

                const title = document.createElement("p")
                div.appendChild(title);
                title.textContent = "TITLE: " + ticket.title;

                const description = document.createElement("p")
                div.appendChild(description);
                description.textContent = "DESCRIPTION: " + ticket.description;

                const id = document.createElement("p")
                div.appendChild(id);
                id.textContent = "ID: " + ticket.id;

                const status = document.createElement("p")
                div.appendChild(status);
                status.textContent = "STATUS: " + ticket.status;

                const priority = document.createElement("p")
                div.appendChild(priority);
                priority.textContent = "PRIORITY: " + ticket.priority;

                const assignedTo = document.createElement("p")
                div.appendChild(assignedTo);
                assignedTo.textContent = "ASSIGNED TO: " + ticket.assigned_to;

                ticketsContainer.appendChild(div);
            })
        })
});

updateButton.addEventListener("click", function(event) {
    updateTicketContainer.textContent = "";
    const div = document.createElement("div");
    div.classList.add("update-ticket");
    const updateForm = document.createElement("form");
    updateForm.classList.add("update-form");

    const idLabel = document.createElement("label");
    idLabel.setAttribute("for", "ticket-id");
    idLabel.textContent = "Ticket ID";

    const idInput = document.createElement("input");
    idInput.setAttribute("id", "ticket-id");
    idInput.setAttribute("type", "number");

    const assignedToLabel = document.createElement("label");
    assignedToLabel.setAttribute("for", "new-assigned-to");
    assignedToLabel.textContent = "New Assigned To";

    const assignedToInput = document.createElement("input");
    assignedToInput.setAttribute("id", "new-assigned-to");
    assignedToInput.setAttribute("type", "text");

    const statusLabel = document.createElement("label");
    statusLabel.setAttribute("for", "new-status");
    statusLabel.textContent = "New Status";

    const statusSelect = document.createElement("select");
    statusSelect.setAttribute("id", "new-status")
    const openOption = document.createElement("option");
    openOption.textContent = "OPEN";
    const inProgressOption = document.createElement("option");
    inProgressOption.value = "IN_PROGRESS";
    inProgressOption.textContent = "IN PROGRESS";
    const resolvedOption = document.createElement("option");
    resolvedOption.textContent = "RESOLVED";
    const closedOption = document.createElement("option");
    closedOption.textContent = "CLOSED"

    const priorityLabel = document.createElement("label");
    priorityLabel.setAttribute("for", "new-priority");
    priorityLabel.textContent = "New Priority";

    const prioritySelect = document.createElement("select");
    prioritySelect.setAttribute("id", "new-priority")
    const lowOption = document.createElement("option");
    lowOption.textContent = "LOW";
    const mediumOption = document.createElement("option");
    mediumOption.textContent = "MEDIUM";
    const highOption = document.createElement("option");
    highOption.textContent = "HIGH";
    const urgentOption = document.createElement("option");
    urgentOption.textContent = "URGENT";

    const updateSubmitButton = document.createElement("button");
    updateSubmitButton.setAttribute("id", "update-submit-button")
    updateSubmitButton.setAttribute("type", "submit");
    updateSubmitButton.textContent = "Submit";

    updateForm.addEventListener("submit", function(event){
        event.preventDefault();

        const ticketData = {
            assigned_to: assignedToInput.value,
            status: statusSelect.value,
            priority: prioritySelect.value
        };
        if (idInput.value.trim() === "") {
            showNotification("Ticket ID cannot be empty", "error");
            return;
        }
        if (assignedToInput.value.trim() === "") {
            showNotification("Ticket assigned to cannot be empty", "error");
            return;
        }
        fetch(`http://127.0.0.1:8000/tickets/${idInput.value}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(ticketData)
        })
        .then(function(response){
            if(response.ok) {
                showNotification("Ticket Updated Successfully", "success");
            }
            if(!response.ok) {
                showNotification("Ticket Update Failed", "error");
            }
        });
    });


    prioritySelect.appendChild(lowOption);
    prioritySelect.appendChild(mediumOption);
    prioritySelect.appendChild(highOption);
    prioritySelect.appendChild(urgentOption);

    statusSelect.appendChild(openOption);
    statusSelect.appendChild(inProgressOption);
    statusSelect.appendChild(resolvedOption);
    statusSelect.appendChild(closedOption);

    updateForm.appendChild(idLabel);
    updateForm.appendChild(idInput);
    updateForm.appendChild(assignedToLabel);
    updateForm.appendChild(assignedToInput);
    updateForm.appendChild(statusLabel);
    updateForm.appendChild(statusSelect);
    updateForm.appendChild(priorityLabel);
    updateForm.appendChild(prioritySelect);
    updateForm.appendChild(updateSubmitButton);
    div.appendChild(updateForm);

    updateTicketContainer.appendChild(div);
});

removeButton.addEventListener("click", function(event){
    removeTicketContainer.textContent = "";
    const div = document.createElement("div");
    div.classList.add("remove-ticket");
    const removeForm = document.createElement("form");
    removeForm.classList.add("remove-form");

    const idLabel = document.createElement("label");
    idLabel.setAttribute("for", "ticket-id");
    idLabel.textContent = "Ticket ID";

    const idInput = document.createElement("input");
    idInput.setAttribute("id", "ticket-id");
    idInput.setAttribute("type", "number");

    const removeConfirmButton = document.createElement("button");
    removeConfirmButton.setAttribute("id", "remove-confirm-button")
    removeConfirmButton.setAttribute("type", "submit");
    removeConfirmButton.textContent = "Confirm delete";

    removeForm.addEventListener("submit", function(event){
        event.preventDefault();
        if (idInput.value.trim() === "") {
            showNotification("Ticket ID cannot be empty", "error");
            return;
        }
        fetch(`http://127.0.0.1:8000/tickets/${idInput.value}`, {
            method: "DELETE",
        })
        .then(function(response){
            if(response.ok) {
                showNotification("Ticket removed successfully", "success");
            }
            if(!response.ok) {
                showNotification("Ticket removal failed", "error");
                }
        });
    })

    removeForm.appendChild(idLabel);
    removeForm.appendChild(idInput);
    removeForm.appendChild(removeConfirmButton);
    div.appendChild(removeForm);

    removeTicketContainer.appendChild(div);
})

createTicketForm.addEventListener("submit", function(event) {
    event.preventDefault();
    const ticketData = {
        title: titleInput.value,
        description: descriptionInput.value,
        assigned_to: assignedToInput.value,
        priority: priorityInput.value
    };
    if (titleInput.value.trim() === "") {
            showNotification("Ticket title cannot be empty", "error");
            return;
        }
    if (descriptionInput.value.trim() === "") {
            showNotification("Ticket description cannot be empty", "error");
            return;
        }
    if (assignedToInput.value.trim() === "") {
            showNotification("Ticket assigned to cannot be empty", "error");
            return;
        }
    fetch("http://127.0.0.1:8000/tickets", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(ticketData)
    })
    .then(function(response){
        if(response.ok) {
            showNotification("Ticket created successfully", "success");
        }
        if(!response.ok) {
            showNotification("Ticket creation failed", "error");
        }
    });
});

function showNotification(message, type) {
    notificationContainer.textContent = "";
    const notification = document.createElement("div");
    notification.classList.add("notification");
    notification.classList.add(type);
    notification.textContent = message;

    notificationContainer.appendChild(notification);
}
