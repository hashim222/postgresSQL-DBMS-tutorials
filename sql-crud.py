from sqlalchemy import(Column, Integer, String, create_engine)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


db = create_engine("postgresql:///chinook")

base = declarative_base()


class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


Session = sessionmaker(db)

session = Session()

base.metadata.create_all(db)

# creating records on our Progammer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

sir_fish = Programmer(
    first_name="Sir",
    last_name="Fish",
    gender="M",
    nationality="Indian",
    famous_for="Last Programmer"
)

session.add(ada_lovelace)
session.add(alan_turing)
session.add(grace_hopper)
session.add(margaret_hamilton)
session.add(bill_gates)
session.add(tim_berners_lee)
session.add(sir_fish)

Programmers = session.query(Programmer)

for prog in Programmers:
    print(
        prog.id,
        prog.first_name + " " + prog.last_name,
        prog.gender,
        prog.nationality,
        prog.famous_for,
        sep=" | "
    )
