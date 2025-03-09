from trame.app import get_server
from trame.widgets import vuetify3 as v3, leaflet3 as l3
from trame.ui.vuetify3 import VAppLayout


class Demo:
    def __init__(self, server=None):
        self.server = get_server(server, client_type="vue3")
        self._build_ui()

    def circle_clicked(self):
        print("circle clicked")

    def _build_ui(self):
        with VAppLayout(self.server, full_height=True) as self.ui:
            v3.VBtn(
                "Reset Zoom ({{zoom}})",
                click="zoom = 16",
                classes="position-absolute bottom-0",
                style="z-index: 1000;",
            )
            with l3.LMap(v_model_zoom=("zoom", 16), center=("[41.89026, 12.49238]",)):
                l3.LTileLayer(
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                    layer_type="base",
                    name="OpenStreetMap",
                )
                l3.LCircleMarker(
                    lat_lng=("[41.89026, 12.49238]",),
                    radius=(50,),
                    click=self.circle_clicked,
                )


def main():
    app = Demo()
    app.server.start()


if __name__ == "__main__":
    main()
