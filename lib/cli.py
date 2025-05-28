import os
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, Member, Trainer, Membership

engine = create_engine('sqlite:///gym.db')
Session = sessionmaker(bind=engine)
session = Session()


def is_initialized():
    """Check if all tables exist in the database."""
    inspector = inspect(engine)
    required_tables = {"members", "trainers", "memberships"}
    existing_tables = set(inspector.get_table_names())
    return required_tables.issubset(existing_tables)


def init_db():
    """Create tables and add some sample data."""
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    trainers = [Trainer(name="Ali"), Trainer(name="Hassan"), Trainer(name="Fatima")]
    memberships = [Membership(type="Monthly"), Membership(type="Yearly")]
    session.add_all(trainers + memberships)
    session.commit()
    print("✅ Database initialized with sample trainers and memberships.")


def show_trainers():
    trainers = session.query(Trainer).all()
    print("\n📋 Available Trainers:")
    for t in trainers:
        print(f"ID: {t.id}, Name: {t.name}")


def show_memberships():
    memberships = session.query(Membership).all()
    print("\n📋 Available Memberships:")
    for m in memberships:
        print(f"ID: {m.id}, Type: {m.type}")


def add_trainer():
    name = input("Enter trainer name: ")
    trainer = Trainer(name=name)
    session.add(trainer)
    session.commit()
    print(f"✅ Added trainer '{name}' with ID {trainer.id}")


def add_membership():
    type_ = input("Enter membership type: ")
    membership = Membership(type=type_)
    session.add(membership)
    session.commit()
    print(f"✅ Added membership '{type_}' with ID {membership.id}")


def add_member():
    if not is_initialized():
        print("❌ Error: Database not initialized. Please run option 1 first.")
        return

    name = input("Enter member name: ")
    show_trainers()
    try:
        trainer_id = int(input("Enter Trainer ID: "))
        trainer = session.query(Trainer).get(trainer_id)
        if not trainer:
            print("❌ Trainer not found.")
            return
    except ValueError:
        print("❌ Invalid Trainer ID.")
        return

    show_memberships()
    try:
        membership_id = int(input("Enter Membership ID: "))
        membership = session.query(Membership).get(membership_id)
        if not membership:
            print("❌ Membership not found.")
            return
    except ValueError:
        print("❌ Invalid Membership ID.")
        return

    member = Member(name=name, trainer_id=trainer_id, membership_id=membership_id)
    session.add(member)
    session.commit()
    print(f"✅ Added member '{name}' with ID {member.id}")


def list_members():
    if not is_initialized():
        print("❌ Error: Database not initialized. Please run option 1 first.")
        return

    members = session.query(Member).all()
    if not members:
        print("ℹ️ No members found.")
        return
    print("\n👥 Members List:")
    for m in members:
        trainer_name = m.trainer.name if m.trainer else "None"
        membership_type = m.membership.type if m.membership else "None"
        print(f"ID: {m.id}, Name: {m.name}, Trainer: {trainer_name}, Membership: {membership_type}")


def main():
    while True:
        print("\n--- Ali fitness zone management ---")
        #print("1. Initialize Database (with sample data)")
        print("2. Add Trainer")
        print("3. Add Membership")
        print("4. Add Member")
        print("5. List Members")
        print("6. List Trainers")
        print("7. List Memberships")
        print("8. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            init_db()
        elif choice == '2':
            add_trainer()
        elif choice == '3':
            add_membership()
        elif choice == '4':
            add_member()
        elif choice == '5':
            list_members()
        elif choice == '6':
            show_trainers()
        elif choice == '7':
            show_memberships()
        elif choice == '8':
            print("👋macsalaamo!")
            break
        else:
            print("❌ Jaribu mara nyingine.")


if __name__ == "__main__":
    main()
