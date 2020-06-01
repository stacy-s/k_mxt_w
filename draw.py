import plotly.express as px
import pandas as pd


class Draw:
    @classmethod
    def draw_points(cls, filename, lat, lon, hover_name, hover_data, color, color_continuous_scale):
        df = pd.read_csv(filename)
        fig = px.scatter_mapbox(df, lat=lat, lon=lon, hover_name=df[color], hover_data=hover_data,
                                color=df[color], zoom=5, height=1000,
                                color_continuous_scale=color_continuous_scale,
                                )
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        fig.show()

