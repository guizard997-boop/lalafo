from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///cars.db")

Base = declarative_base()


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True)
    link = Column(String, unique=True)
    title = Column(String)
    price = Column(Integer)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


def is_new(link):
    db = Session()
    result = db.query(Car).filter_by(link=link).first()
    db.close()

    return result is None


def save_car(link, title, price):
    db = Session()

    car = Car(
        link=link,
        title=title,
        price=price
    )

    db.add(car)
    db.commit()
    db.close()