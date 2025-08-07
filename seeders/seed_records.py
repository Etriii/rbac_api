from app.db import engine
from app.models import LotsOfDataForPagination
from faker import Faker
from sqlmodel import Session

faker = Faker()


def create_datas(n=200):

    with Session(engine) as session:
        users = [LotsOfDataForPagination(name=faker.name()) for _ in range(n)]
        session.add_all(users)
        session.commit()

    print(f"Added {n} users")


create_datas()
