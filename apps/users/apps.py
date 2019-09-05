from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # 配置信号
    def ready(self):
        import users.signals
