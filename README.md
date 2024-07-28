# 2048
Exploration into python flask for the (formerly popular) 2048 game.

## Versioning
Written with python 3.12.3

## Run app (python)
``` 
cd ../2048/app
python app.py 
```
Then go to 'http://localhost:5000'

## Run app (docker)
```
cd ../2048

#build
./build.sh

#run
./deploy.sh

#(Optional) exec
docker exec -it 'container ID' /bin/bash
```
Then go to 'http://localhost:5000'

```
#clean and delete
./delete.sh
```
