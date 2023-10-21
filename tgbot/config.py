from dataclasses import dataclass

from environs import Env
@dataclass
class DbConfig:
    host: str
    port: int
    password: str
    user: str
    database: str

@dataclass
class RedisConfig:
    enable: bool
    host: str
    port: int
    password: str
    database: int

@dataclass
class TgBot:
    debug: bool
    token: str
    admin_ids: list[int]


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tgbot: TgBot
    database: DbConfig
    redis: RedisConfig
    misc: Miscellaneous


env = Env()
env.read_env()

config = Config(
    tgbot=TgBot(
        debug=env.bool("DEBUG"),
        token=env.str("BOT_TOKEN"),
        admin_ids=list(map(int, env.list("ADMINS"))),

    ),
    database=DbConfig(
        host=env.str('DB_HOST'),
        port=env.int('DB_PORT'),
        password=env.str('DB_PASS'),
        user=env.str('DB_USER'),
        database=env.str('DB_NAME')
    ),
    redis=RedisConfig(
        enable=env.bool("REDIS_ENABLE"),
        host=env.str('REDIS_HOST'),
        port=env.int('REDIS_PORT'),
        password=env.str('REDIS_PASS'),
        database=env.str('REDIS_DATABASE')
    ),
    misc=Miscellaneous()
)