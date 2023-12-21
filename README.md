# Cartridge monitoring

Проект - мониторинг заправки картриджей, в котором администратор ведет запись заказов. А пользователи отслеживают статус работ по заправке картриджей.

**Стек:**
+ [Python](https://www.python.org/downloads/)
+ [Django](https://www.djangoproject.com/)
+ [SQLite3](https://docs.python.org/3/library/sqlite3.html#module-sqlite3)


### Документация к проекту: [doc](documentation%2Fproject_documentation.md).

## Локальная разработка:

Все действия должны выполняться из исходного каталога проекта и только после установки всех требований.

1. Во-первых, создайте и активируйте новую виртуальную среду:

```shell
python -m venv venv
venv\Scripts\activate
```

2. Инициализируйте git-репозиторий:

```shell
git init 
```

3. Клонируйте репозиторий.


4. Установите файл зависимостей:

```shell
pip install --upgrade pip
pip install -r requirements.txt
```

5. Запуск зависимостей проекта, миграции, заполнение базы данных данными (если необходимо - для тестирования работы):

```shell
python manage.py migrate
python manage.py loaddata <path_to_fixture_files>
```
  **Примечание 1:** файл фикстур в проекте находиться по следующему пути:
  + app/fixtures/orders.json

  **Примечание 2:** после загрузки фикстур может потребоваться выполнить команды:

  ```shell
  python manage.py makemigration 
  python manage.py migrate
  ```

6. Запустите сервер:

```shell
python manage.py runserver
```

После успешного запуска, проект будет доступен по адресу: http://127.0.0.1:8000/