## Сервис управления рассылками, администрирования и получения статистики.
### Сервис направлен на удержание текущих клиентов для распростронения «прогревающих» рассылок с целью информирования и привлечения клиентов. 
Проект разрабатывался на дистрибутиве Ubuntu(Linux Mint)

Прядок запуска проекта:

- установите файл .env и внесите свои ключи безопастности в константы находящиеся в шаблоне .env.template

- установите брокер Redis
```angular2html
pip install redis
```
- установите пакет django-celery-beat
```angular2html
pip install django-celery-beat
```
-  установите виртуальную среду venv
```angular2html
python3 -m venv venv
```
- активируйте виртуальную среду
```angular2html
 source venv/bin/activate
```
- установите утилиты из файла [requirements.txt](requirements.txt)

- примените миграции
```angular2html
python manage.py migrate
```
- выполните команду для установки суперюзера, пароль и логин для входа находятся в файле [csu.py](clients%2Fmanagement%2Fcommands%2Fcsu.py)
```angular2html
python3 manage.py csu
```
- права пользователей распределяются на странице администратора в гуппе Менеджер
```angular2html
127.0.0.1:8000/admin/
```
- запустите celery в первом терминале
```angular2html
celery -A clients worker -l info
```
- запустите celery-beat во втором терминале
```angular2html
celery -A clients beat -l INFO
```
- выполните скрипт рассылки, который работает как из командой строки, так и по расписанию.
```angular2html
python3 manage.py mail_sender
```
- при желании загрузите фикстуры)
```angular2html
python3 manage.py loaddata clients_data.json
```
```angular2html
python3 manage.py loaddata blog_data.json
```
- запустите сервер django и перейдите по ссылке [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
```angular2html
python3 manage.py runserver
```
- перед закрытием IDE остановите сервер django
```angular2html
pkill -f runserver
```
P.S При попытке пользователя работать не со своим клиентом или рассылкой программа выдаст ошибку Http404

