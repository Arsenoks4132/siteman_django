# О проекте

Информационный сайт с применением Django и Django REST FRAMEWORK, содержащий информацию об известных людях.

# 1. Клонирование репозитория

Склонируйте репозиторий с исходным кодом и тестами:

```bash
git clone <URL репозитория>
cd <директория проекта>
```

# 2. Виртуальное окружение

```shell
python -m venv venv
venv\Scripts\activate
```

# 3. Установка зависимостей

```shell
pip install -r requirements.txt
```

# 4. Применение миграциф и загрузка фикстур

```shell
py siteman/manage.py makemigrations && py siteman/manage.py loaddata siteman/db.json
```

# 4. Запуск программы

```shell
py siteman/manage.py runserver 80
```