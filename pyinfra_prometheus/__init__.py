# pyinfra prometheus
# File: pyinfra_prometheus/__init__.py
# Desc: export deploys and install/configure helper function

from pyinfra.api import deploy

from .prometheus import configure_prometheus, install_prometheus
from .node_exporter import configure_node_exporter, install_node_exporter


@deploy('Deploy prometheus')
def deploy_prometheus(state, host, enable_service=True):
    install_prometheus(state, host)
    configure_prometheus(state, host, enable_service=enable_service)
    install_node_exporter(state, host)
    configure_node_exporter(state, host, enable_service=enable_service)
