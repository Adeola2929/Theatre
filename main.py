from fastapi import FastAPI
from routers import seatRoute, ticketRoute
app = FastAPI()
# Routers

app.include_router(seatRoute.seat_router)
app.include_router(ticketRoute.ticket_router)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "🎭Welcome to the Sierra Leone Theatre"}
