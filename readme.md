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


7 start both container
docker start tryflaskdemo_db_1

docker start tryflaskdemo_web_1

8 check python file
docker exec -it tryflaskdemo_web_1 bash
