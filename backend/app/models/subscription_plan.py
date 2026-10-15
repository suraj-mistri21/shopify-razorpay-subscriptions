from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class SubscriptionPlan(Base):
    __tablename__ = "subscription_plans"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    shopify_product_id: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        index=True,
    )

    shopify_variant_id: Mapped[str] = mapped_column(
        String(64),
        unique=True,
        nullable=False,
    )

    razorpay_plan_id: Mapped[str | None] = mapped_column(
        String(100),
        unique=True,
        nullable=True,
    )

    amount_paise: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    currency: Mapped[str] = mapped_column(
        String(3),
        default="INR",
        nullable=False,
    )

    billing_interval: Mapped[str] = mapped_column(
        String(20),
        default="monthly",
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )