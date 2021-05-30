# ServerIOT
##Install Postgresql
1.sudo apt update
2.sudo apt install postgresql postgresql-contrib
3. set password postgres = root

##Install poetry
4 . curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
5. source $HOME/.poetry/env
6. poetry shell
7. poetry install 
8. cd demo
9. python3 manage.py makemigrations
10. python3 manage.py migrate
11. python3 manage.py runserver
