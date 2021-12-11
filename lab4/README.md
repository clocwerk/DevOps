# Lab4

### 1. Ознайомився з Docker
### 2. Перевірив чи встановлений докер і виконав наступні команди
#### docker -v
#### docker -h
#### docker run docker/whalesay cowsay Docker is fun
#### Перенаправив вивід цих команд у файл my_work.log закомітив до репозиторію
### 3. Ознайомився з документацією
### 4. Виконав команди 
#### sudo docker pull python:3.8-slim
#### sudo docker images
#### sudo docker inspect python:3.8-slim
### 5. Створив власний репозиторій на Docker Hub.
### 6. Виконав білд імеджа та завантажив його до репозеторію за допомогою команд :
#### sudo docker build -t clokwerk/lab4:django .
#### sudo docker images 
#### sudo docker push clokwerk/lab4:django .
#### Посилання на Docker:[`Docker`](https://hub.docker.com/r/clokwerk/lab4)
#### Посилання на скачування імеджа:[`Docker`](https://hub.docker.com/layers/clokwerk/lab4/django/images/sha256-d1e1d99a2ac02976ed19c74b8191718bde223270e6ff642748a91f53ddfe5022?context=explore)
### 7.Для запуску веб-сайту виконав команду
    docker run -it --name=django --rm -p 8000:8000 clokwerk/lab4:django
### Сайт працює
### 8. Створив файл Dockerfile.site 
### 9. Виконав білд даного імеджа docker build -t clokwerk/lab4:monitoring .
#### Посилання :[`docker`](https://hub.docker.com/layers/clokwerk/lab4/monitoring/images/sha256-d1e1d99a2ac02976ed19c74b8191718bde223270e6ff642748a91f53ddfe5022?context=explore)
### 10.Переконався,що програма виконується успішно. Виконав команду
#### sudo docker run -it --rm -p 8000:8000 --net=host clokwerk/lab4:monitoring

 
 
