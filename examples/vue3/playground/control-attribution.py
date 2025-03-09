from trame.app import get_server
from trame.widgets import vuetify3 as v3, leaflet3 as l3
from trame.ui.vuetify3 import VAppLayout


class Demo:
    def __init__(self, server=None):
        self.server = get_server(server, client_type="vue3")
        self._build_ui()

    def _build_ui(self):
        with VAppLayout(self.server, full_height=True) as self.ui:
            v3.VBtn(
                "Reset Zoom ({{zoom}})",
                click="center = [47.41322, -1.219482]; zoom = 2;",
                classes="position-absolute top-0 right-0 ma-4",
                style="z-index: 1000;",
            )
            with l3.LMap(
                v_model_zoom=("zoom", 2),
                v_model_center=("center", [47.41322, -1.219482]),
            ):
                l3.LTileLayer(
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                    layer_type="base",
                    name="OpenStreetMap",
                )
                l3.LControlAttribution(
                    position="bottomleft",
                    prefix=(
                        "customAttributionPrefix",
                        "<strong>Custom bottom left attribution</strong>",
                    ),
                )


def main():
    app = Demo()
    app.server.start()


if __name__ == "__main__":
    main()
