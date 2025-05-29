from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, Trainer, Membership, Member


engine = create_engine('sqlite:///gym.db')
Session = sessionmaker(bind=engine)
session = Session()

def seed():
    
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    
    trainer1 = Trainer(name="Alice")
    trainer2 = Trainer(name="Bob")
    session.add_all([trainer1, trainer2])
    session.commit()

   
    membership1 = Membership(type="Monthly")
    membership2 = Membership(type="Yearly")
    session.add_all([membership1, membership2])
    session.commit()

    
    member1 = Member(name="John Doe", trainer_id=trainer1.id, membership_id=membership1.id)
    member2 = Member(name="Jane Smith", trainer_id=trainer2.id, membership_id=membership2.id)
    session.add_all([member1, member2])
    session.commit()

    print("Database seeded successfully.")

if __name__ == "__main__":
    seed()