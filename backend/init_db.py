from app.models.user_model import User, Customer, Seller
from app.models.product_model import Product
from sqlmodel import SQLModel
from app.core.db import engine


def init_db():
    print("Initializing database...")
    SQLModel.metadata.create_all(engine)
    print("Tables created successfully.")
