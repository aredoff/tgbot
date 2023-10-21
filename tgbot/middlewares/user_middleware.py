from telebot.handler_backends import BaseMiddleware
from tgbot.models.user import User

class UserMiddleware(BaseMiddleware):
    update_types = ['message']
    def pre_process(self, message, data):
        user, _ = User.get_or_create(
            telegram_id=message.from_user.id,
            defaults={
                'username': message.from_user.username,
                'first_name': message.from_user.first_name,
                'language_code': message.from_user.language_code,
            })
        data["user"] = user

    def post_process(self, message, data, exception):
        pass
