from sqlalchemy import Column, BigInteger, func, DateTime, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    count = Column(Integer, default=100)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
    available_credit = Column(Float, default=1000)
    remaining_credit = Column(Float, default=1000)


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("customer.id"))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
