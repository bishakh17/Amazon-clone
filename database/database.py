import sqlalchemy as sql

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:5503@localhost:3306/ecommerce"
engine = sql.create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sql.orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = sql.ext.declarative.declarative_base()


