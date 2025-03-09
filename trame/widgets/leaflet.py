from trame_leaflet.widgets.leaflet import *  # noqa F401


def initialize(server):
    from trame_leaflet.module import leaflet2

    server.enable_module(leaflet2)
