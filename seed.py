from models import Pet, db
from app import app


db.drop_all()
db.create_all()

olive = Pet(name="Olive", species="dog", photo_url="https://images.pexels.com/photos/825949/pexels-photo-825949.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500", age=3, notes="This dog is stanky")

castiel = Pet(name="Castiel", species="dog", photo_url="https://images.pexels.com/photos/3687770/pexels-photo-3687770.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", age=5, notes="This is a naughty boy")

ramen = Pet(name="Ramen", species="cat", photo_url="https://images.pexels.com/photos/127028/pexels-photo-127028.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500", age=2, notes="This cat is rude")

macaroni = Pet(name="Macaroni", species="cat", photo_url="https://images.pexels.com/photos/1170986/pexels-photo-1170986.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500", age=1, notes="This is a chonker")

matt = Pet(name="Matt", species="fish", photo_url="https://images.pexels.com/photos/128756/pexels-photo-128756.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", age=1, notes="This fish is nice", available=False)

db.session.add_all([olive, castiel, ramen, macaroni, matt])

db.session.commit()

