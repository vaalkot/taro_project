import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session


SqlAlchemyBase = orm.declarative_base()

__factory = None

def global_init(db_file):
    global __factory

    if __factory:
        return

    if not db_file:
        raise Exception("Не указано имя файла базы данных.")

    engine = sa.create_engine(f"sqlite:///{db_file}?check_same_thread=False", echo=False)
    __factory = orm.sessionmaker(bind=engine)
    SqlAlchemyBase.metadata.create_all(engine)

def create_session() -> Session:
    global __factory
    return __factory()
