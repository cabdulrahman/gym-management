"""
A simple debug script for inspecting your gym management database.
You can use this to quickly check the contents of your tables.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, Trainer, Member, Membership

def print_trainers(session):
    print("\n--- Trainers ---")
    trainers = session.query(Trainer).all()
    if not trainers:
        print("No trainers found.")
    for t in trainers:
        print(f"ID: {t.id}, Name: {t.name}")

def print_memberships(session):
    print("\n--- Memberships ---")
    memberships = session.query(Membership).all()
    if not memberships:
        print("No memberships found.")
    for m in memberships:
        print(f"ID: {m.id}, Type: {m.type}")

def print_members(session):
    print("\n--- Members ---")
    members = session.query(Member).all()
    if not members:
        print("No members found.")
    for m in members:
        trainer_name = m.trainer.name if m.trainer else "None"
        membership_type = m.membership.type if m.membership else "None"
        print(f"ID: {m.id}, Name: {m.name}, Trainer: {trainer_name}, Membership: {membership_type}")

def main():
    engine = create_engine('sqlite:///gym.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    print("Welcome to the Gym Management Debugger!")
    print_trainers(session)
    print_memberships(session)
    print_members(session)

if __name__ == "__main__":
    main()