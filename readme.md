1
sudo apt-get install docker-compose

2
if have issue:
Name or service not known',)': /simple/flask/

restart docker


3 run
docker-compose build

4
docker-compose up

5 check Mongo
docker start tryflaskdemo_db_1

6 to db
docker exec -it tryflaskdemo_db_1 mongo admin
