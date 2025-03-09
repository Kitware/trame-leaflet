from trame.app import get_server
from trame.widgets import leaflet3 as l3, vuetify3 as v3
from trame.ui.vuetify3 import VAppLayout


class Demo:
    def __init__(self, server=None):
        self.server = get_server(server, client_type="vue3")
        self._build_ui()

    def _build_ui(self):
        with VAppLayout(self.server, full_height=True) as self.ui:
            v3.VLabel(
                "({{location}})",
                classes="position-absolute bottom-0",
                style="z-index: 1000;",
            )

            with l3.LMap(v_model_zoom=("zoom", 2), center=("[47.41322, -1.219482]",)):
                l3.LTileLayer(
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                    layer_type="base",
                    name="OpenStreetMap",
                )
                l3.LMarker(
                    v_model_lat_lng=("location", [50, 50]),
                    draggable=True,
                )


def main():
    app = Demo()
    app.server.start()


if __name__ == "__main__":
    main()
