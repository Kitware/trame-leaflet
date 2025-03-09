from trame.app import get_server
from trame.widgets import leaflet3 as l3
from trame.ui.vuetify3 import VAppLayout


class Demo:
    def __init__(self, server=None):
        self.server = get_server(server, client_type="vue3")
        self._build_ui()

    def _build_ui(self):
        with VAppLayout(self.server, full_height=True) as self.ui:
            with l3.LMap(
                v_model_zoom=("zoom", 2),
                v_model_center=("center", [47.41322, -1.219482]),
            ):
                l3.LTileLayer(
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                    layer_type="base",
                    name="OpenStreetMap",
                )
                l3.LControlZoom(
                    position="bottomleft",
                    zoom_in_text="*",
                    zoom_out_text="/",
                )


def main():
    app = Demo()
    app.server.start()


if __name__ == "__main__":
    main()
