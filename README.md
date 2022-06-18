# mirrori-exercise
## the Mirrori  Backend Developer Position Exercise

## endpoints

- `/post` - a POST endpoint that manages the creation of a new message
- `/getall` - a GET endpoint that allows querying all the messages sent so far
- `/stream` - a GET endpoint that streams new messages as they are received

## usage


```sh
git clone https://github.com/bruhmomentu/mirrori-exercise.git
docker-compose up --build -d --scale pycharm-project=2
```

# testing
terminal 1:
```sh
curl --no-buffer 127.0.0.1:5000/stream
```
terminal 2:
```sh
curl 127.0.0.1:5000/post -d '{"message": "Welcome"}' -H 'Content-Type: application/json'
curl 127.0.0.1:5000/post -d '{"message": "to Mirrori"}' -H 'Content-Type: application/json'
curl 127.0.0.1:5000/getall
```
 now both terminals should look like this:
 ```
 Welcome
 to Mirrori
 ```

# info
i started this project with basic knowledge in python and knowledge in networking, as for redis, flask and docker i googled a lot and now i know how to use flask and redis (still not so sure about the docker)
