from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class LocalSQLite:
    def __init__(self):
        self._database = None

    @property
    def database(self):
        if not self._database:
            engine = create_engine("sqlite:///fruit.db")
            Session = sessionmaker(bind=engine)
            self._database = Session()
        return self._database


sqlite = LocalSQLite()
sql_alchemy_db = sqlite.database


def initialize_database() -> None:
    from fruit.src.models import Base

    engine = create_engine("sqlite:///fruit.db")
    Base.metadata.create_all(bind=engine)


def destroy_database() -> None:
    from fruit.src.models import Base

    engine = create_engine("sqlite:///fruit.db")
    Base.metadata.drop_all(bind=engine)
