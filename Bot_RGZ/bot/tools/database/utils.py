from . import engine, models
from sqlalchemy.orm import Session

# from . import engine, models импортирует объекты engine и models из текущего пакета (текущей директории).
#
# engine является экземпляром create_engine из модуля sqlalchemy. Он представляет собой движок базы данных,
# который обеспечивает связь с базой данных и выполнение запросов.
#
# models представляет модуль или пакет, содержащий определения моделей (таблиц) базы данных.
# В этом случае, предполагается, что модели находятся в файле models.py в текущем пакете.
#
# from sqlalchemy.orm import Session импортирует класс Session из модуля sqlalchemy.orm.
# Session представляет сеанс работы с базой данных и используется для выполнения запросов и управления транзакциями.

def get_median_price(name):
    with Session(engine) as session:
        security = session.query(models.Security).filter(models.Security.security_name == name).first()
        if security is not None and security.is_active == True:
            return security.median_price
        else:
            return None

# Функция get_median_price получает имя ценной бумаги в качестве аргумента name.
#
# Внутри функции создается сеанс (Session) работы с базой данных, используя engine.
#
# Затем выполняется запрос к таблице Security с помощью метода query с указанием модели models.Security.
# В запросе применяется фильтр, чтобы найти запись, у которой значение поля security_name соответствует переданному имени name.
#
# Метод first() возвращает первую найденную запись, удовлетворяющую условиям запроса.
#
# Если найдена запись и значение поля is_active равно True, то функция возвращает значение поля median_price из найденной записи.
#
# Если запись не найдена или значение поля is_active равно False, функция возвращает None.


def set_add_user_security(tg_id,name):
    with Session(engine) as session:
        session.add(models.Users(
            tg_id= tg_id,
            security_name=name
        ))
        session.commit()

# Функция set_add_user_security добавляет новую запись пользователя в базу данных.
# Она принимает два аргумента: tg_id (идентификатор пользователя) и name (имя ценной бумаги).
# Внутри функции создается сеанс работы с базой данных,
# создается новый экземпляр модели Users с переданными значениями, и этот экземпляр добавляется в сеанс.
# Затем изменения сохраняются в базе данных вызовом метода commit().

def set_new_security(name):
    with Session(engine) as session:
        session.add(models.Security(
            security_name=name
        ))
        session.commit()

# Функция set_new_security добавляет новую запись о ценной бумаге в базу данных.
# Она принимает один аргумент name (имя ценной бумаги).
# Внутри функции создается сеанс работы с базой данных, создается новый экземпляр модели Security с
# переданным именем, и этот экземпляр добавляется в сеанс.
# Затем изменения сохраняются в базе данных вызовом метода commit().

def set_add_security(name, price):
        with Session(engine) as session:
            security = session.query(models.Security).filter(models.Security.security_name == name).first()
            if (security != None):
                security.median_price = price
            session.commit()

# Функция set_add_security обновляет запись о ценной бумаге в базе данных с указанием новой цены.
# Она принимает два аргумента: name (имя ценной бумаги) и price (новая цена).
#
# Внутри функции создается сеанс работы с базой данных. Затем выполняется запрос к базе данных,
# чтобы найти запись о ценной бумаге с указанным именем. Если такая запись найдена (security != None),
# то обновляется значение median_price у найденной записи. Затем изменения сохраняются в базе данных вызовом
# метода commit().


def set_security_disable(name):
    with Session(engine) as session:
        security = session.query(models.Security).filter(models.Security.security_name == name).first()
        if (security != None):
            security.is_active = False
        session.commit()

# Функция set_security_disable отключает ценную бумагу в базе данных,
# устанавливая флаг is_active в значение False. Она принимает один аргумент name,
# который указывает имя ценной бумаги.
#
# Внутри функции создается сеанс работы с базой данных. Затем выполняется запрос к базе данных,
# чтобы найти запись о ценной бумаге с указанным именем. Если такая запись найдена (security != None), то
# устанавливается значение is_active в False у найденной записи. Затем изменения сохраняются в базе данных
# вызовом метода commit(). Это позволяет отключить ценную бумагу и предотвратить ее использование в будущих
# операциях или расчетах.

def get_name_security(name):
    with Session(engine) as session:
        security_name = session.query(models.Security).filter(models.Security.security_name == name).first()
        return security_name

# Функция get_name_security возвращает объект ценной бумаги из базы данных по указанному имени.
# Она принимает один аргумент name, который указывает имя ценной бумаги.


def get_name_security_users(tg_id,name):
    with Session(engine) as session:
        user = session.query(models.Users).filter(models.Users.tg_id == tg_id).all()
        if user != None :
            for a in user:
                 if a.security_name == name:
                    return True
        else:
            return None

# Функция get_name_security_users проверяет, есть ли у пользователя с указанным tg_id ценная бумага с
# указанным именем name в его портфеле.
#
# Внутри функции создается сеанс работы с базой данных. Затем выполняется запрос к базе данных для получения всех
# записей о пользователе с указанным tg_id. Если записи о пользователе найдены, происходит проверка каждой записи.
# Если имя ценной бумаги в записи соответствует указанному имени, функция возвращает значение True, что указывает
# на наличие ценной бумаги в портфеле пользователя. Если ни одна запись не соответствует условию, возвращается
# значение None, что означает, что у пользователя нет ценной бумаги с указанным именем в портфеле.

def get_len_security():
    mas = []
    with Session(engine) as session:
        name = session.query(models.Security).all()
        for a in name:
            if a.is_active:
                mas.append(a.security_name)
        return mas

# Функция get_len_security возвращает список активных ценных бумаг из базы данных.
#
# Внутри функции создается сеанс работы с базой данных. Затем выполняется запрос к базе данных для получения
# всех записей о ценных бумагах. Для каждой записи происходит проверка на активность (is_active). Если ценная
# бумага активна, ее имя добавляется в список mas. После обработки всех записей возвращается список mas, содержащий
# имена активных ценных бумаг.
#

def get_security(tg_id):
    mas = []
    with Session(engine) as session:
        user = session.query(models.Users).filter(models.Users.tg_id == tg_id).all()
        if user != None :
            for a in user:
                mas.append(a.security_name)
            return mas
        else:
            return None

# Функция get_security возвращает список ценных бумаг, связанных с заданным tg_id.
#
# Внутри функции создается сеанс работы с базой данных. Затем выполняется запрос к базе данных для получения
# всех записей о пользователях с заданным tg_id. Если найдены записи, происходит итерация по каждой записи и
# добавление имени ценной бумаги в список mas. В конце функции возвращается список mas, содержащий имена ценных
# бумаг, связанных с заданным tg_id. Если не найдено ни одной записи, возвращается None.