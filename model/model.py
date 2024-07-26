from model.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(999))
    password = Column(String(999))
    name = Column(String(999))
    user_type_id = Column(Integer, ForeignKey("user_types.id"))

    type = relationship("UserType", back_populates="type_users")


class UserType(Base):

    __tablename__ = "user_types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(999))

    type_users = relationship("User", back_populates="type")


# class Stock(Base):
#     __tablename__ = "stocks"

#     id = Column(Integer, primary_key=True, index=True)
#     categorie_id = Column(Integer, ForeignKey("categories.id"))

#     categorie = relationship("Cotegorie", back_populates="stocks")


# class SubCategorie(Base):
#     __tablename__ = "sub_categories"

#     id = Column(Integer, primary_key=True, index=True)
#     dom_categorie_id = Column(Integer, ForeignKey("categories.id"))
#     sub_categorie_id = Column(Integer, ForeignKey("categories.id"))

#     dom = relationship(
#         "Cotegorie", back_populates="dom_categorie", foreign_keys=[dom_categorie_id]
#     )
#     sub = relationship(
#         "Cotegorie", back_populates="sub_categorie", foreign_keys=[sub_categorie_id]
#     )


# class Transaction(Base):
#     __tablename__ = "transactions"

#     id = Column(Integer, primary_key=True, index=True)
#     input = Column(Boolean)
#     amount = Column(Integer)
#     transaction_time = Column(DateTime)
#     items_id = Column(Integer, ForeignKey("items.id"))

#     item = relationship("Item", back_populates="transactions")


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(999))
#     count = Column(Integer)
#     quantity_id = Column(Integer, ForeignKey("quantities.id"))
#     categorie_id = Column(Integer, ForeignKey("categories.id"))

#     transactions = relationship("Transaction", back_populates="item")

#     quantity = relationship("Quantity", back_populates="items")
#     categirie = relationship("Cotegorie", back_populates="items")


# class Cotegorie(Base):
#     __tablename__ = "categories"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(999))

#     stocks = relationship("Stock", back_populates="categorie")
#     items = relationship("Item", back_populates="categorie")

#     dom_categorie = relationship("SubCategorie", back_populates="dom")
#     sub_categorie = relationship("SubCategorie", back_populates="sub")


# class Quantity(Base):
#     __tablename__ = "quantities"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(999))

#     items = relationship("Item", back_populates="quantity")
