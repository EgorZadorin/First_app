# First_app

## Зависимости

Приложение написано на языке Python 3 и использует базу данных PostgreSQL. Сервер БД должен быть [установлен](https://www.postgresqltutorial.com/install-postgresql/).

Конфигурация подключения находится в файле config.py и может быть изменена:
```python3
db_config = {
'host': '127.0.0.1',
'port': 5432,
'dbname': 'first_app',
'user': 'first_user',
'pass': 'first_pass'
}
```

Необходимые пакеты указаны в файле requirements.txt

## Установка

Убедиться в наличии актуальной версии python3 (3.6 +)
```
python3 --version
```

Установить необходимые пакеты
```
pip3 install -r requirements.txt
```

## Запуск

```
python3 app.py
```

Приложение запустится на порте 4000, номер порта можно изменить в файле config.py
