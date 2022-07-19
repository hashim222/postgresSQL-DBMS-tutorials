from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "Artist" table


class Students(base):
    __tablename__ = "Student Details"
    student_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

hashim = Students(
    first_name="Hashim",
    last_name="Aslam"
)

# session.add(hashim)
# session.commit()

# stds = session.query(Students)
# for std in stds:
#     if std.student_id == 2:
#         session.delete(std)
#         session.commit()

stds = session.query(Students)
for std in stds:
    if std.student_id == 2:
        std.student_id = 3

students = session.query(Students)
for student in students:
    print(
        student.student_id,
        student.first_name,
        student.last_name
    )
