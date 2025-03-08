from trame.app import get_server
from trame.widgets import vuetify3 as v3, leaflet3 as l3
from trame.ui.vuetify3 import SinglePageLayout


# -----------------------------------------------------------------------------
# Initialization
# -----------------------------------------------------------------------------
server = get_server(client_type="vue3")
state, ctrl = server.state, server.controller

state.trame__title = "Leaflet3 Trame WebApp"


def event(name, value):
    print(name, value)


# -----------------------------------------------------------------------------
# GUI
# -----------------------------------------------------------------------------

with SinglePageLayout(server, fill_height=True) as layout:
    layout.title.set_text("Leaflet Trame WebApp")

    with layout.toolbar:
        v3.VProgressLinear(
            indeterminate=True,
            absolute=True,
            bottom=True,
            active=("trame__busy",),
        )

    with layout.content:
        with v3.VContainer(
            fluid=True,
            classes="pa-0 fill-height",
        ) as c:
            with l3.LMap(
                v_model_zoom=("zoom", 15),
                center=("center", [51.505, -0.159]),
                move=("console.log(['lmap:move', $event])"),
            ):
                l3.LTileLayer(
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                )
                # l3.LControlLayers()
                with l3.LMarker(
                    lat_lng=("marker_pos1", [51.504, -0.159]),
                    draggable=True,
                    move_end="console.log('LMarker:moveend 1', $event)",
                ):
                    l3.LTooltip("LOL 1")

                with l3.LMarker(
                    lat_lng=("marker_pos2", [50, 50]),
                    draggable=True,
                    move_end=("console.log(['LMarker:moveend 2', $event])"),
                ):
                    l3.LTooltip("LOL 2")

                l3.LPolyline(
                    color="green",
                    lat_lngs=(
                        "polyline",
                        [
                            [47.334852, -1.509485],
                            [47.342596, -1.328731],
                            [47.241487, -1.190568],
                            [47.234787, -1.358337],
                        ],
                    ),
                )
                l3.LPolygon(
                    color="#41b782",
                    fill=True,
                    fill_opacity=0.5,
                    fill_color="#41b782",
                    lat_lngs=(
                        "polygon",
                        [
                            [46.334852, -1.509485],
                            [46.342596, -1.328731],
                            [46.241487, -1.190568],
                            [46.234787, -1.358337],
                        ],
                    ),
                )
                l3.LRectangle(
                    fill=True,
                    color="#35495d",
                    lat_lngs=(
                        "rect",
                        [
                            [46.334852, -1.509485],
                            [46.342596, -1.328731],
                            [46.241487, -1.190568],
                            [46.234787, -1.358337],
                        ],
                    ),
                )
                with l3.LRectangle(
                    bounds=(
                        "rect_b",
                        [
                            [46.334852, -1.190568],
                            [46.241487, -1.090357],
                        ],
                    )
                ):
                    l3.LPopup("LOL 4")

            print(c)


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    server.start()
