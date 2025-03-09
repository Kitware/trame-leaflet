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
                click="zoom = 11",
                classes="position-absolute bottom-0",
                style="z-index: 1000;",
            )
            with l3.LMap(v_model_zoom=("zoom", 11), center=("[44.48865, 11.3317]",)):
                l3.LTileLayer(
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                    layer_type="base",
                    name="OpenStreetMap",
                )
                l3.LCircle(
                    lat_lng=("[44.48865, 11.3317]",),
                    radius=(5000,),
                    color="green",
                    click=self.circle_clicked,
                )


def main():
    app = Demo()
    app.server.start()


if __name__ == "__main__":
    main()
