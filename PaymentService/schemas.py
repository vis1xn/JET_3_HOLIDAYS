from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal

class PaymentCreate(BaseModel):
    user_id: int
    booking_id: int
    amount: float = Field(gt=0, description="Payment amount must be positive")
    payment_method: Literal["credit_card", "debit_card", "paypal", "bank_transfer"]

class Payment(PaymentCreate):
    payment_id: int
    payment_date: datetime
    status: Literal["completed", "pending", "failed", "refunded"]

    class Config:
        orm_mode = True