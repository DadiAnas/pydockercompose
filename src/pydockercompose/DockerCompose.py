import yaml


class DockerCompose:
    """
    This class represent docker-compose file.
    In this version it support adding the following parameters:
        -  version
        -  services
        -  volumes
        -  networks

    A parameter can be an object of other classes, string or a dictionary.
    """

    def __str__(self):
        self.clean_yaml()
        return self._docker_file.__str__()

    def __init__(self, file_name: str = "docker-compose.yml", version: str = "2.2", services: dict = {},
                 volumes: dict = {}, networks: dict = {}):
        """
        :param file_name: the docker compose file name.
        :param version: Docker compose version to use.
        :param services: Docker compose services.
        :param volumes: Docker compose volumes.
        :param networks: Docker compose networks.
        """
        self._file_name = file_name
        self._version = version
        self._services = services
        self._volumes = volumes
        self._networks = networks
        self._docker_file = {
            "version": version,
            "services": self._services,
            "volumes": self._volumes,
            "networks": self._networks,
        }

    def add_service(self, name, service):
        """
        This function helps to add a service to the :param services.
        It returns true if the service added, False otherwise.

        :param name: Service name.
        :param service: A docker-compose file service. It can be an instance of Service class  or dictionary.
        :return: True if the service is well added.
        """
        try:
            self._services[name] = service.clean_service()
            return True
        except Exception:
            raise Exception

    def add_network(self, name, network: dict):
        """
        This function helps to add a service to the :param networks.
        It returns true if the service added, False otherwise.

        :param name: Network name.
        :param network: A docker-compose file network. It can be an instance of Service class  or dictionary.
        :return: void
        """
        try:
            self._networks[name] = network
        except Exception:
            raise Exception

    def add_volumes(self, name: str, volumes: dict):
        """
        This function helps to add a volume to the :param volumes.
        It returns true if the service added, False otherwise.

        :param name: the network name.
        :param volumes: A docker-compose file volume. It can be an object of Volume class or a dictionary.
        :return: void
        """
        try:
            self._volumes[name] = volumes
        except Exception:
            raise Exception

    def clean_yaml(self):
        """
        This function help to remove None, [] , "" and {} from the docker_file parameter.
        :return: void
        """
        try:
            filtered = {k: v for k, v in self._docker_file.items() if v if v not in (None, [], "", {})}
            self._docker_file.clear()
            self._docker_file.update(filtered)
        except Exception:
            raise Exception

    def to_yaml(self, path: str = "./"):
        self.clean_yaml()
        with open(path + self._file_name, 'w') as docker_compose_file:
            yaml.dump(self._docker_file, docker_compose_file)


