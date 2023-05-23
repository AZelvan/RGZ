from sqlalchemy import MetaData, Table, String, Integer, Float, Column, Text,Boolean
from sqlalchemy.orm import declarative_base
from . import engine

# from sqlalchemy import MetaData, Table, String, Integer, Float, Column, Text, Boolean
# импортирует необходимые классы и типы данных из модуля SQLAlchemy.
# from sqlalchemy.orm import declarative_base импортирует функцию declarative_base из модуля SQLAlchemy ORM.
# Эта функция используется для создания базового класса, который будет использоваться для определения моделей данных.
# from . import engine импортирует объект engine из текущего пакета.

# После выполнения этих строк кода, вы можете использовать импортированные классы и объекты для определения
# моделей данных и выполнения операций с базой данных с помощью SQLAlchemy.

Base = declarative_base()


# Base = declarative_base() создает базовый класс для определения моделей данных в SQLAlchemy.

# Обычно в SQLAlchemy каждая модель данных должна быть производной от базового класса declarative_base().
# Это позволяет использовать преимущества SQLAlchemy ORM, такие как отображение объектно-реляционной модели,
# отслеживание изменений объектов и выполнение запросов к базе данных.

class Security(Base):
    __tablename__ = 'security'

    id = Column(Integer, primary_key=True)
    security_name = Column(String(255), nullable=False)
    median_price = Column(String(255))
    is_active = Column(Boolean, default=True)


# Класс Security является моделью данных для таблицы "security".
# Он наследуется от базового класса Base и определяет структуру таблицы и ее столбцов.
#
# __tablename__ - атрибут класса, определяющий имя таблицы в базе данных.
# id - столбец типа Integer, который является первичным ключом таблицы.
# security_name - столбец типа String(255), представляющий название ценной бумаги.
# Он не может быть пустым (nullable=False).
# median_price - столбец типа String(255), представляющий медианную цену ценной бумаги.
# is_active - столбец типа Boolean, определяющий активность ценной бумаги. По умолчанию установлено значение True.
# Эта модель данных позволяет работать с таблицей "security" в базе данных, создавать,
# изменять и получать информацию о ценных бумагах.

class Users(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer, nullable=False)
    security_name = Column(String(255))


# Класс Users является моделью данных для таблицы "user".
# Он также наследуется от базового класса Base и определяет структуру таблицы и ее столбцов.
#
# __tablename__ - атрибут класса, определяющий имя таблицы в базе данных.
# id - столбец типа Integer, который является первичным ключом таблицы.
# tg_id - столбец типа Integer, представляющий идентификатор пользователя Telegram.
# Он не может быть пустым (nullable=False).
# security_name - столбец типа String(255), представляющий название ценной бумаги, связанной с пользователем.
# Эта модель данных позволяет работать с таблицей "user" в базе данных, хранить информацию о пользователях и их
# связанных ценных бумагах.

Base.metadata.create_all(bind=engine)

# Base.metadata.create_all(bind=engine) является вызовом метода create_all() на метаданных базового класса Base.
# Этот метод создает все таблицы, определенные в метаданных, в базе данных, связанной с указанным движком (engine).
#
# Таким образом, вызов Base.metadata.create_all(bind=engine) создаст все таблицы, определенные в моделях
# Security и Users, в базе данных, связанной с указанным движком engine.