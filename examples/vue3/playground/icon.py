from trame.app import get_server, asynchronous
from trame.widgets import leaflet3 as l3
from trame.ui.vuetify3 import VAppLayout

import aiohttp


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                return f"Error: {response.status}"


class Demo:
    def __init__(self, server=None):
        self.server = get_server(server, client_type="vue3")
        self._build_ui()
        asynchronous.create_task(self.fetch_geojson())

    async def fetch_geojson(self):
        url = "https://rawgit.com/gregoiredavid/france-geojson/master/regions/pays-de-la-loire/communes-pays-de-la-loire.geojson"
        with self.server.state as state:
            state.geojson = await fetch_data(url)

    def _build_ui(self):
        with VAppLayout(self.server, full_height=True) as self.ui:
            with l3.LMap(
                v_model_zoom=("zoom", 8),
                v_model_center=("center", [47.41322, -1.219482]),
            ):
                l3.LTileLayer(
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                    layer_type="base",
                    name="OpenStreetMap",
                )
                with l3.LMarker(
                    lat_lng=("[47.41322, -1.219482]",),
                ):
                    l3.LIcon(
                        icon_url="https://picsum.photos/200/100",
                        icon_size=("[200, 100]",),
                    )


def main():
    app = Demo()
    app.server.start()


if __name__ == "__main__":
    main()
