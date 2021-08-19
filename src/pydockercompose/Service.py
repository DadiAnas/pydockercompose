class Service:
    def __init__(self, container_name: str = "", image: str = "", build: str = "", restart: str = "", ports: list = [],
                 networks: list = [], volumes: list = [],
                 environments: list = [], depends_on: list = [], commands: str = "", links=[], network_mode: str=""):
        self._image = image
        self._container_name = container_name
        self._depends_on = depends_on
        self._restart = restart
        self._build = build
        self._volumes = volumes
        self._ports = ports
        self._environment = environments
        self._commands = commands
        self._networks = networks
        self._ulimits = {}
        self._service = {}
        self._links = links
        self._network_mode = network_mode

    def set_image(self, image):
        self._image = image

    def set_container_name(self, image):
        self._image = image

    def set_depends_on(self, image):
        self._image = image

    def set_build(self, image):
        self._image = image

    def set_restart(self, restart_type="always"):
        self._restart = restart_type

    def set_ulimits(self, limit_type, params_dict):
        self._ulimits[limit_type] = params_dict

    def add_volume(self, volume):
        self._volumes.append(volume)

    def add_network(self, network):
        self._networks.append(network)

    def add_port(self, port):
        self._ports.append(port)

    def add_environment_variable(self, variable):
        self._environment.append(variable)

    def set_commands(self, command):
        self._commands = command

    def set_network_mode(self, network_mode):
        self._network_mode = network_mode

    def clean_service(self):
        self._service = {
            "image": self._image,
            "build": self._build,
            "container_name": self._container_name,
            "environment": self._environment,
            "restart": self._restart,
            "ports": self._ports,
            "volumes": self._volumes,
            "networks": self._networks,
            "ulimits": self._ulimits,
            "links": self._links,
            "depends_on": self._depends_on,
            "command": self._commands,
            "network_mode": self._network_mode,
        }
        filtered = {k: v for k, v in self._service.items() if v not in (None, [], "", {})}
        self._service.clear()
        self._service.update(filtered)
        return self._service
