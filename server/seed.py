#!/usr/bin/env python3

from app import app
from models import db, Plant

def seed_database():
    with app.app_context():
        # Clear existing data
        Plant.query.delete()
        
        # Create plants with specific IDs
        aloe = Plant(
            id=1,
            name="Aloe",
            image="./images/aloe.jpg",
            price=11.50,
            is_in_stock=True,
        )

        zz_plant = Plant(
            id=2,
            name="ZZ Plant",
            image="./images/zz-plant.jpg",
            price=25.98,
            is_in_stock=False,
        )
        
        # Add more plants if needed for testing
        monstera = Plant(
            id=3,
            name="Monstera",
            image="./images/monstera.jpg",
            price=30.00,
            is_in_stock=True,
        )

        db.session.add_all([aloe, zz_plant, monstera])
        db.session.commit()
        print("Database seeded successfully!")
        print(f"Created plants with IDs: 1, 2, 3")

if __name__ == '__main__':
    seed_database()