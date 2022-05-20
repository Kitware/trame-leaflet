from trame.app import get_server
from trame.assets.local import LocalFileManager
from trame.widgets import vuetify, leaflet
from trame_client.widgets.core import Template
from trame.ui.vuetify import SinglePageWithDrawerLayout


# -----------------------------------------------------------------------------
# Initialization
# -----------------------------------------------------------------------------
server = get_server()
state, ctrl = server.state, server.controller

state.trame__title = "Leaflet Trame WebApp"

# -----------------------------------------------------------------------------
# GUI
# -----------------------------------------------------------------------------

with SinglePageWithDrawerLayout(server) as layout:
    layout.title.set_text("Leaflet Trame WebApp")

    with layout.toolbar:
        vuetify.VSpacer()
        vuetify.VSwitch(
            hide_details=True,
            v_model=("$vuetify.theme.dark",),
        )
        vuetify.VProgressLinear(
            indeterminate=True,
            absolute=True,
            bottom=True,
            active=("trame__busy",),
        )

    with layout.drawer:
        vuetify.VContainer()

    with layout.content:
        with vuetify.VContainer(
            fluid=True,
            classes="pa-0 fill-height",
        ):
            with leaflet.LMap(zoom=("zoom", 15), center=("center", [51.505, -0.159])):
                leaflet.LTileLayer(
                    url=("url", "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"),
                    attribution=(
                        "attribution",
                        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
                    ),
                )
                # leaflet.VGeosearch(options=("options",{"provider": "OpenStreetMapProvider"}))
                leaflet.LMarker(lat_lng=("markerLatLng", [51.504, -0.159]))



# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    server.start()
