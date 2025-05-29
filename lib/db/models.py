from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Trainer(Base):
    __tablename__ = 'trainers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    members = relationship('Member', back_populates='trainer')

class Membership(Base):
    __tablename__ = 'memberships'
    id = Column(Integer, primary_key=True)
    type = Column(String, nullable=False)
    member = relationship('Member', back_populates='membership', uselist=False)

class Member(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    trainer_id = Column(Integer, ForeignKey('trainers.id'))
    membership_id = Column(Integer, ForeignKey('memberships.id'))
    trainer = relationship('Trainer', back_populates='members')
    membership = relationship('Membership', back_populates='member')

