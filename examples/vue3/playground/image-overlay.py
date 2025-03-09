from trame.app import get_server
from trame.widgets import leaflet3 as l3
from trame.ui.vuetify3 import VAppLayout


class Demo:
    def __init__(self, server=None):
        self.server = get_server(server, client_type="vue3")
        self._build_ui()

    @property
    def state(self):
        return self.server.state

    def _build_ui(self):
        self.state.update(
            {
                "width": 100,
                "height": 100,
                "bounds": [
                    [0, 0],
                    [100, 100],
                ],
                "markers": [
                    {"coordinates": {"lng": 0, "lat": 0}},
                    {"coordinates": {"lng": 100, "lat": 0}},
                    {"coordinates": {"lng": 0, "lat": 100}},
                    {"coordinates": {"lng": 100, "lat": 100}},
                    {"coordinates": {"lng": 0, "lat": 50}},
                    {"coordinates": {"lng": 50, "lat": 0}},
                    {"coordinates": {"lng": 50, "lat": 100}},
                    {"coordinates": {"lng": 100, "lat": 50}},
                ],
            }
        )
        with VAppLayout(self.server, full_height=True) as self.ui:
            with l3.LMap(
                v_model_zoom=("zoom", 1),
                center=("[width/2, height/2]",),
                min_zoom=-5,
            ):
                l3.LImageOverlay(
                    url="https://www.printablee.com/postpic/2011/06/blank-100-square-grid-paper_405041.jpg",
                    bounds=("bounds",),
                )
                with l3.LMarker(
                    v_for="(marker, idx) in markers",
                    key="idx",
                    lat_lng=("marker.coordinates",),
                ):
                    l3.LPopup("{{ idx }}")


def main():
    app = Demo()
    app.server.start()


if __name__ == "__main__":
    main()
