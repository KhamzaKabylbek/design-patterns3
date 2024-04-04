import os
from dotenv import dotenv_values
import threading

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        # Загрузка общих переменных разработки
        shared_config = dotenv_values(".env.shared")

        # Загрузка чувствительных переменных
        secret_config = dotenv_values(".env.secret")

        # Переопределение загруженных значений переменными среды
        env_config = os.environ

        # Объединение всех конфигураций
        self.config = {**shared_config, **secret_config, **env_config}

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = cls()
        return cls._instance

    def execute_query(self, query):
        # Выполнение SQL-запроса
        pass

    def get_results(self):
        # Получение результатов запроса
        pass

# Тестовая программа
def test_singleton():
    # Создание двух экземпляров DatabaseConnection
    instance1 = DatabaseConnection.get_instance()
    instance2 = DatabaseConnection.get_instance()

    # Проверка, что оба экземпляра одинаковы
    assert instance1 is instance2

    # Получение информации о подключении к базе данных
    print(instance1.config)

if __name__ == "__main__":
    test_singleton()
