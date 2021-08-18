# pydockercompose 
## Description

This package is a python package for generating Docker Compose file.
It contains two classes :
*   DockerCompose : which represent represent docker-compose file.
    In this version, it supports adding the following parameters:
       -  version
       -  services
       -  volumes
       -  networks
*   Service: This class represent docker compose service. 
    In this version, Service class supports adding the following parameters:
    *   image
    *   build
    *   container_name
    *   environment
    *   restart
    *   ports
    *   volumes
    *   networks
    *   ulimits
    *   links

To find out more about these parameters, you can check [docker-compose](https://docs.docker.com/compose/compose-file/compose-file-v3/) documentation.

## Usecase

In this example we used `pydockercompose` package to generate `docker-compose.yml` for :
- ElasticSearch service
- ElasticSearch Client service that will be built using Dockerfile.

        import pydockercompose
        import os,sys

        def generate_elastic_docker_compose_file():
            docker_compose = DockerCompose(version="3.3")
        
            # Create ElasticSearch service.
            elastic_svc = Service(container_name="es",
                                  image="elasticsearch:7.13.3",
                                  restart="on-failure",
                                  ports=["9200:9200"],
                                  networks=["es-network"],
                                  volumes=["es-data:/usr/share/elasticsearch/data"],
                                  environments=["discovery.type=single-node"])
            elastic_svc.set_ulimits("memlock", {"soft": -1, "hard": -1})
        
            # Create ElasticSearch Customer service.
            cmd = "while [ 1 -e 1 ]; do curl 'http://es:9200/' && sleep 3 ; done"
            with open("Dockerfile", "w") as dockerfile:
                dockerfile.write("FROM alpine:3\nRUN apk add curl\nCMD "+cmd)
            customer_svc = Service(container_name="es-customer",
                                   build=".",
                                   restart="on-failure",
                                   depends_on=["es"],
                                   networks=["es-network"])
        
            # Add services to DockerCompose object.
            docker_compose.add_service("es", elastic_svc)
            docker_compose.add_service("es-customer", customer_svc)
        
            # Add the network es-network
            docker_compose.add_network("es-network", {"driver": "bridge"})
        
            # Add the volume es-data
            docker_compose.add_volumes("es-data", {"driver": "local"})
            return docker_compose
        
        
        if __name__ == '__main__':
            generate_elastic_docker_compose_file().to_yaml()
            os.system("docker-compose up")
