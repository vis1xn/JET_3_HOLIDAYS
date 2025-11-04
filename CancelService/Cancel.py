from fastapi import APIRouter, HTTPException, status
import httpx

CancelService = APIRouter()

# URL of the BookingService microservice
BOOKING_SERVICE_URL = "http://localhost:8001"  # Adjust port as needed

@CancelService.delete("/api/flights/cancel/{booking_id}", status_code=status.HTTP_200_OK)
async def cancel_booking(booking_id: int):
    async with httpx.AsyncClient() as client:
        try:
            # Call BookingService to delete the booking
            response = await client.delete(
                f"{BOOKING_SERVICE_URL}/api/flights/book/{booking_id}"
            )
            
            if response.status_code == 404:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Booking with ID {booking_id} not found"
                )
            
            response.raise_for_status()
            
            return {
                "message": "Booking cancelled successfully",
                "booking_id": booking_id
            }
            
        except httpx.RequestError as e:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="BookingService is unavailable"
            )