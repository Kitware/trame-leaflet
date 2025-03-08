from trame_leaflet.widgets.leaflet3 import *  # noqa F403


def initialize(server):
    from trame_leaflet.module import leaflet3

    server.enable_module(leaflet3)
