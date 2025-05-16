import sqlalchemy as sa
from .db_session import SqlAlchemyBase

class Cards(SqlAlchemyBase):
    __tablename__ = 'cards'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String, nullable=False)
    spread = sa.Column(sa.String, nullable=False)
    photo = sa.Column(sa.String, nullable=True)
