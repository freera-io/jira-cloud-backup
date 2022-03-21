from app.config import Settings, get_settings
from loguru import logger as log
import sys
import motor.motor_asyncio
import asyncio
# from redisworks import Root

def get_logger():
    log.remove()
    log.add(sys.stdout, colorize=True, format='<level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | <level>{message}</level>')
    return log

conf = get_settings()

class DI_Container:
    cfg: Settings = conf
    log = get_logger()
    mongo = motor.motor_asyncio.AsyncIOMotorClient(conf.mongo_dsn, serverSelectionTimeoutMS=5000)


