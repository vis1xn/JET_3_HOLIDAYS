from fastapi import APIRouter, HTTPException, status
from .schemas import Payment, PaymentCreate
from datetime import datetime

PaymentService = APIRouter()

payments = []

@PaymentService.post("/api/payments", status_code=status.HTTP_201_CREATED)
def create_payment(payment: PaymentCreate):
    new_payment = Payment(
        payment_id=len(payments) + 1,
        payment_date=datetime.now(),
        status="completed",
        **payment.model_dump()
    )
    payments.append(new_payment)
    return new_payment

@PaymentService.get("/api/payments", status_code=status.HTTP_200_OK)
def get_all_payments():
    return {"payments": payments, "count": len(payments)}

@PaymentService.get("/api/payments/{payment_id}", status_code=status.HTTP_200_OK)
def get_payment(payment_id: int):
    for p in payments:
        if p.payment_id == payment_id:
            return p
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Payment not found"
    )

@PaymentService.get("/api/payments/booking/{booking_id}", status_code=status.HTTP_200_OK)
def get_payments_by_booking(booking_id: int):
    booking_payments = [p for p in payments if p.booking_id == booking_id]
    if not booking_payments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No payments found for this booking"
        )
    return {"payments": booking_payments, "count": len(booking_payments)}

@PaymentService.get("/api/payments/user/{user_id}", status_code=status.HTTP_200_OK)
def get_payments_by_user(user_id: int):
    user_payments = [p for p in payments if p.user_id == user_id]
    if not user_payments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No payments found for this user"
        )
    return {"payments": user_payments, "count": len(user_payments)}

@PaymentService.put("/api/payments/{payment_id}/refund", status_code=status.HTTP_200_OK)
def refund_payment(payment_id: int):
    for idx, p in enumerate(payments):
        if p.payment_id == payment_id:
            if p.status == "refunded":
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Payment already refunded"
                )
            payments[idx].status = "refunded"
            return {
                "message": f"Payment {payment_id} refunded successfully",
                "payment": payments[idx]
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Payment not found"
    )