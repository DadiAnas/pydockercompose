class Service:
    """
    This class represent 'service' in docker compose file.
    """

    def __init__(self, container_name: str = "", image: str = "", build: str = "", restart: str = "", ports: list = [],
                 networks: list = [], volumes: list = [],
                 environments: list = [], depends_on: list = [], entrypoint: str = "", command: str = "", links=[],
                 network_mode: str = ""):
        """
        :param container_name: The name of the container.
        :param image: The image of the container to build from image. Example: image = "alpine:latest"
        :param build: The path to Dockerfile to build image using it. Example: build = "."
        :param restart: Type of the restart. Example: restart = "Always".
        :param ports: List of ports. Example: ports = ["80:80","22:22"]
        :param networks: List of networks. Example: networks = ["my_network_0","my_network_1"]
        :param volumes: List of volumes. Example: volumes = ["my_volume_0","my_volume_1"]
        :param environments: Environment variables. Example: volumes = ["my_volume_0","my_volume_1"]
        :param depends_on: Dependencies services.
        :param command: Command to execute. Example: command = "bundle exec thin -p 3000".
        :param entrypoint: Override the default entrypoint. Example: entrypoint = "/code/entrypoint.sh"
        :param links: List of services names to link with. Example: links = ["db:database", "redis"]
        :param network_mode: Network mode. Example: network_mode = "bridge"
        """
        self._container_name = container_name
        self._image = image
        self._build = build
        self._restart = restart
        self._ports = ports
        self._networks = networks
        self._volumes = volumes
        self._environment = environments
        self._depends_on = depends_on
        self._command = command
        self._entrypoint = entrypoint
        self._links = links
        self._ulimits = {}
        self._network_mode = network_mode
        self._service = {}

    def set_container_name(self, container_name: str = ""):
        self._container_name = container_name

    def set_image(self, image: str = ""):
        self._image = image

    def set_build(self, build: str = ""):
        self._build = build

    def set_restart(self, restart_type: str = "always"):
        self._restart = restart_type

    def set_ports(self, ports: list = []):
        self._ports = ports

    def set_networks(self, networks: list = []):
        self._networks = networks

    def set_volumes(self, volumes: list = []):
        self._volumes = volumes

    def set_environment(self, environment: list = []):
        self._environment = environment

    def set_depends_on(self, depends_on: list = []):
        self._depends_on = depends_on

    def set_command(self, command: str = ""):
        self._command = command

    def set_entrypoint(self, entrypoint: str = ""):
        self._entrypoint = entrypoint

    def set_links(self, links: list = []):
        self._links = links

    def set_ulimits(self, limit_type, params_dict: dict):
        self._ulimits[limit_type] = params_dict

    def set_network_mode(self, network_mode: str = ""):
        self._network_mode = network_mode

    def add_volume(self, volume: str):
        self._volumes.append(volume)

    def add_network(self, network: str):
        self._networks.append(network)

    def add_port(self, port: str):
        self._ports.append(port)

    def add_environment_variable(self, variable):
        self._environment.append(variable)

    def add_depends_on_service(self, service_name: str):
        self._depends_on.append(service_name)

    def add_link_service(self, link_service_name: str):
        self._links.append(link_service_name)

    def clean_service(self):
        self._service = {
            "container_name": self._container_name,
            "image": self._image,
            "build": self._build,
            "environment": self._environment,
            "restart": self._restart,
            "ports": self._ports,
            "volumes": self._volumes,
            "networks": self._networks,
            "ulimits": self._ulimits,
            "links": self._links,
            "depends_on": self._depends_on,
            "command": self._commands,
            "entrypoint": self._entrypoint,
            "network_mode": self._network_mode,
        }
        filtered = {k: v for k, v in self._service.items() if v not in (None, [], "", {})}
        self._service.clear()
        self._service.update(filtered)
        return self._service
