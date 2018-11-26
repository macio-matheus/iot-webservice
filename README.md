# IoT WebService
WebService for interaction with a NodeMCU device 

### Architecture

![Architecture]()

## Usage
First of all, build the container using docker-compose and then you can 
access the Jupyter that is ready to be used.

##### Run with docker compose
```sh
cd iot-webservice
docker-compose up -d --build
```

##### Accessing Jupyter
```sh
http://<your-ip>:8888/tree
```

##### Ports
```sh
    - 8888 => Jupyter
    - 6007 => Tensorboard
    - 5007 => Your App
```

## DockerHub
```sh
https://hub.docker.com/r/maciomatheus/jupyter_notebook_data_science/
```

##### Arduino dependences
```sh
    ArduinoJson:5.13.3
```