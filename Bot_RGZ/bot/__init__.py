from aiogram import Dispatcher, Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from .tools import task
from apscheduler.schedulers.asyncio import AsyncIOScheduler


# from aiogram import Dispatcher, Bot, executor:
# Импортирует классы Dispatcher, Bot и executor из модуля aiogram.
# Эти классы являются основными компонентами для создания и управления ботом с
# использованием фреймворка aiogram.
#
# from aiogram.contrib.fsm_storage.memory import MemoryStorage:
# Импортирует класс MemoryStorage из модуля aiogram.contrib.fsm_storage.memory.
# MemoryStorage представляет собой хранилище состояний (FSM) в памяти, которое используется для сохранения состояний пользователей и их контекста во время работы бота.
#
# from .tools import task: Импортирует модуль или пакет task из текущего пакета
# Это позволяет использовать функционал из модуля task в текущем модуле.
#
# from apscheduler.schedulers.asyncio import AsyncIOScheduler:
# Импортирует класс AsyncIOScheduler из модуля apscheduler.schedulers.asyncio.
# AsyncIOScheduler представляет собой планировщик задач, который позволяет выполнять определенные задачи
# в заданное время или с определенной периодичностью, используя асинхронный подход.
#
# Общий смысл этих импортов заключается в подключении необходимых модулей и компонентов для работы с aiogram,
# хранения состояний, выполнения задач и настройки приложения.
#


bot = Bot(token='5970269169:AAGQLHRkhQXkzUY-tm77mVqpVZyhWqqGCw0')
dp = Dispatcher(bot, storage=MemoryStorage())

# В этом участке кода создаются объекты bot и dp, которые используются
# для взаимодействия с ботом и управления его функциональностью.
#
# bot = Bot(token=config.TOKEN): Создает объект bot типа Bot из модуля aiogram.
# Для инициализации объекта Bot необходимо указать токен вашего бота.
# Токен предоставляется при регистрации бота на платформе Telegram.
#
# dp = Dispatcher(bot, storage=MemoryStorage()): Создает объект dp типа Dispatcher из модуля aiogram.
# Dispatcher представляет собой центральный компонент, который отслеживает и обрабатывает входящие события
# от пользователя (сообщения, команды, колбэки и т.д.) и определяет, какие обработчики должны быть вызваны для
# каждого события. В конструкторе Dispatcher передается объект bot для связи между ними, а также создается и
# используется экземпляр MemoryStorage в качестве хранилища состояний (FSM).
#
# Создание объектов bot и dp является важной частью настройки бота с использованием фреймворка aiogram.
# Они предоставляют основные функции для отправки и получения сообщений, управления состояниями,
# регистрации обработчиков и многое другое.

def register_handlers():
    from .handlers import commands,addSecurity,securitiesPerformance
    commands.register_handlers(dp)
    addSecurity.register_handlers(dp)
    securitiesPerformance.register_handlers(dp)



# Функция register_handlers предназначена для регистрации обработчиков событий в диспетчере dp.
#
# from .handlers import commands,addSecurity,securitiesPerformance:
# Импортирует модули commands, addSecurity и securitiesPerformance из пакета handlers.
# Предполагается, что эти модули содержат определения функций-обработчиков для соответствующих событий.
#
# commands.register_handlers(dp): Вызывает функцию register_handlers из модуля commands и передает ей объект dp.
# Эта функция регистрирует обработчики команд в диспетчере.
#
# addSecurity.register_handlers(dp): Вызывает функцию register_handlers из модуля addSecurity и передает ей объект dp.
# Эта функция регистрирует обработчики, связанные с добавлением ценных бумаг, в диспетчере.
#
# securitiesPerformance.register_handlers(dp): Вызывает функцию register_handlers из модуля
# securitiesPerformance и передает ей объект dp. Эта функция регистрирует обработчики,
# связанные с показателями ценных бумаг, в диспетчере.
#
# Этот код объединяет обработчики событий из разных модулей, регистрирует их в диспетчере dp и связывает их с
# соответствующими событиями. Таким образом, когда происходит событие
# (например, пользователь отправляет команду или нажимает кнопку),
# соответствующий обработчик будет вызываться для обработки этого события.




def scheduled_job():
    scheduler = AsyncIOScheduler()
    # scheduler.add_job(task.start_calculate, 'cron', hour=10)
    scheduler.add_job(task.start_calculate, 'interval', seconds=120)
    scheduler.start()

# Функция scheduled_job создает планировщик задач scheduler с использованием AsyncIOScheduler из модуля apscheduler.

#
# scheduler = AsyncIOScheduler(): Создает экземпляр планировщика задач scheduler с использованием класса
# AsyncIOScheduler. Этот планировщик позволяет выполнять задачи асинхронно в среде asyncio.
#
# # scheduler.add_job(task.start_calculate, 'cron', hour=10): Это комментарий, который описывает как добавить задачу,
# запускающую функцию task.start_calculate по расписанию. В данном случае, закомментирована строка
# с использованием расписания cron для выполнения задачи в определенное время (10:00 часов).
# Если вам нужно запустить задачу по расписанию,
# вы можете раскомментировать эту строку и настроить соответствующие параметры расписания.
#
# scheduler.add_job(task.start_calculate, 'interval', seconds=120):
# Добавляет задачу, запускающую функцию task.start_calculate через равные интервалы времени.
# В данном случае, задача будет выполняться каждые 120 секунд (2 минуты) меньше НЕЛЬЗЯ иначе ответы на запрос на сервер будут приходить None
#
# scheduler.start(): Запускает планировщик задач. После вызова этого метода,
# планировщик начнет запускать добавленные задачи согласно их расписанию или интервалу.
#
# Этот код настраивает планировщик задач для выполнения функции task.start_calculate в
# определенные моменты времени или через заданные интервалы времени.
# Вы можете настроить планировщик для выполнения других задач по вашим требованиям,
# изменяя параметры вызова scheduler.add_job.

def start_bot():
    register_handlers()
    scheduled_job()
    executor.start_polling(dp, skip_updates=True)

# Функция start_bot запускает бота и выполняет несколько шагов для его настройки.
#
# register_handlers(): Вызывает функцию register_handlers, которая регистрирует обработчики команд и коллбэков в
# диспетчере dp. В этой функции происходит импорт модулей handlers и регистрация соответствующих обработчиков команд
# и коллбэков.
#
# scheduled_job(): Вызывает функцию scheduled_job, которая настраивает планировщик задач для выполнения определенной
# задачи в определенное время или через заданные интервалы времени.
#
# executor.start_polling(dp, skip_updates=True): Запускает бота в режиме "прослушивания" (polling) с
# использованием диспетчера dp. Бот будет получать обновления и обрабатывать их, вызывая соответствующие обработчики.
#
# В целом, эта функция связывает все необходимые шаги для запуска бота,
# включая регистрацию обработчиков, настройку планировщика задач и запуск бота в режиме прослушивания обновлений.
#
#
