from dataclasses import dataclass
from environs import Env


@dataclass
class BotINFO:
    bot_token: str


@dataclass
class DataBaseINFO:
    database_url: str


@dataclass
class Config:
    bot_info: BotINFO
    database_info: DataBaseINFO


def load_config() -> Config:
    env = Env()
    env.read_env()

    return Config(bot_info=BotINFO(bot_token=env('BOT_TOKEN')),
                  database_info=DataBaseINFO(database_url=env('DATABASE_URL')))


config = load_config()