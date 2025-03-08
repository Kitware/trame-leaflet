from trame.app import get_server
from trame.widgets import vuetify3 as v3, leaflet3 as l3
from trame.ui.vuetify3 import SinglePageWithDrawerLayout


# -----------------------------------------------------------------------------
# Initialization
# -----------------------------------------------------------------------------
server = get_server(client_type="vue3")
state, ctrl = server.state, server.controller

state.trame__title = "Leaflet3 Trame WebApp"

# -----------------------------------------------------------------------------
# GUI
# -----------------------------------------------------------------------------

with SinglePageWithDrawerLayout(server) as layout:
    layout.title.set_text("Leaflet Trame WebApp")

    with layout.toolbar:
        v3.VProgressLinear(
            indeterminate=True,
            absolute=True,
            bottom=True,
            active=("trame__busy",),
        )

    with layout.drawer:
        v3.VContainer()

    with layout.content:
        with v3.VContainer(
            fluid=True,
            classes="pa-0 fill-height",
        ) as c:
            with l3.LMap(zoom=("zoom", 15), center=("center", [51.505, -0.159])):
                l3.LTileLayer(
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                    layer_type="base",
                    name="OpenStreetMap",
                    attribution=(
                        "attribution",
                        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                    ),
                )
                l3.LMarker(lat_lng=("markerLatLng", [51.504, -0.159]))

            print(c)


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    server.start()
