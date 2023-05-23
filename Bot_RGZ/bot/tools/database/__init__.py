from sqlalchemy import create_engine


engine = create_engine('postgresql://postgres:password@localhost:5432/for_RGZ')
connection = engine.connect()

from .utils import *

# create_engine('postgresql://postgres:password@localhost:5432/nameDatabase')
# создает объект движка SQLAlchemy для подключения к базе данных PostgreSQL.
# Он использует строку подключения 'postgresql://userName:password@localhost:5432/nameDatabase',
# которая содержит информацию о хосте (localhost), порте (5432), имени пользователя (userName), пароле (password)
# и названии базы данных (nameDatabase).
# engine.connect() устанавливает соединение с базой данных, используя созданный движок SQLAlchemy.
# Результатом является объект соединения, который можно использовать для выполнения операций базы данных.
# from .utils import * импортирует все символы (функции, классы, переменные) из модуля utils,
# находящегося в том же пакете, что и текущий модуль.