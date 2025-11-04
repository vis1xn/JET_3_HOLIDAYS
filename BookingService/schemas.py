from pydantic import BaseModel
from datetime import date, time

class FlightBookingBase(BaseModel):
    user_id: int
    flight_number: str
    departure_airport: str
    arrival_airport: str
    departure_date: date
    departure_time: time
    arrival_time: time

class FlightBookingCreate(FlightBookingBase):
    pass

class FlightBooking(FlightBookingBase):
    booking_id: int

    class Config:
        orm_mode = True