from fastapi import APIRouter, HTTPException, status
from .schemas import FlightBooking, FlightBookingCreate

FlightService = APIRouter()

bookings = []

@FlightService.post("/api/flights/book", status_code=status.HTTP_201_CREATED)
def create_booking(booking: FlightBookingCreate):
    new_booking = FlightBooking(booking_id=len(bookings) + 1, **booking.dict())
    bookings.append(new_booking)
    return new_booking
