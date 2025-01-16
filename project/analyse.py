import pandas as pd
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
import geopandas as gpd

from urllib.request import urlopen
import json

with urlopen(
    "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"
) as response:
    counties = json.load(response)
df = pd.read_csv("data/results.csv", index_col=0)
print(df.corr())

fips_map = {
    "ALBANY": "36001",
    "ALLEGANY": "36003",
    "BRONX": "36005",
    "BROOME": "36007",
    "CATTARAUGUS": "36009",
    "CAYUGA": "36011",
    "CHAUTAUQUA": "36013",
    "CHEMUNG": "36015",
    "CHENANGO": "36017",
    "CLINTON": "36019",
    "COLUMBIA": "36021",
    "CORTLAND": "36023",
    "DELAWARE": "36025",
    "DUTCHESS": "36027",
    "ERIE": "36029",
    "ESSEX": "36031",
    "FRANKLIN": "36033",
    "FULTON": "36035",
    "GENESEE": "36037",
    "GREENE": "36039",
    "HAMILTON": "36041",
    "HERKIMER": "36043",
    "JEFFERSON": "36045",
    "KINGS": "36047",
    "LEWIS": "36049",
    "LIVINGSTON": "36051",
    "MADISON": "36053",
    "MONROE": "36055",
    "MONTGOMERY": "36057",
    "NASSAU": "36059",
    "NEWYORK": "36061",
    "NIAGARA": "36063",
    "ONEIDA": "36065",
    "ONONDAGA": "36067",
    "ONTARIO": "36069",
    "ORANGE": "36071",
    "ORLEANS": "36073",
    "OSWEGO": "36075",
    "OTSEGO": "36077",
    "PUTNAM": "36079",
    "QUEENS": "36081",
    "RENSSELAER": "36083",
    "RICHMOND": "36085",
    "ROCKLAND": "36087",
    "STLAWRENCE": "36089",
    "SARATOGA": "36091",
    "SCHENECTADY": "36093",
    "SCHOHARIE": "36095",
    "SCHUYLER": "36097",
    "SENECA": "36099",
    "STEUBEN": "36101",
    "SUFFOLK": "36103",
    "SULLIVAN": "36105",
    "TIOGA": "36107",
    "TOMPKINS": "36109",
    "ULSTER": "36111",
    "WARREN": "36113",
    "WASHINGTON": "36115",
    "WAYNE": "36117",
    "WESTCHESTER": "36119",
    "WYOMING": "36121",
    "YATES": "36123",
}


print(df.corr())
# print(df.head())

corr_matrix = df.corr()

mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

masked_corr = corr_matrix.mask(mask)

fig = go.Figure(
    data=go.Heatmap(
        z=masked_corr.values,
        x=masked_corr.columns,
        y=masked_corr.index,
        colorscale="Thermal",
        colorbar=dict(tickfont=dict(size=10)),
    )
)

fig.update_layout(
    title={
        "text": "Correlation",
        "x": 0.5,
        "xanchor": "center",
        "font": {"size": 14},
    },
    xaxis=dict(tickfont=dict(size=10), title_font=dict(size=24)),
    yaxis=dict(tickfont=dict(size=10), title_font=dict(size=24), autorange="reversed"),
    margin=dict(l=50, r=50, t=50, b=50),
)
fig.show()
fig.write_image(f"corr.png", "png")


def normalise_county_name(s):
    s = s.replace(" County, New York", "").upper()
    translation_table = str.maketrans({".": None, ",": None, " ": None})
    s = s.translate(translation_table)
    return s


# Annahme: df hat eine Spalte "value_column" mit den Werten, nach denen eingefärbt werden soll.
value_column = "Rural Percent"  # Ersetze dies durch den Namen der Spalte, die du einfärben möchtest.

df["fips"] = df.index.map(fips_map)
df["county_name"] = df.index
for c in df.columns:
    if c == "fips" or c == "county_name":
        continue
    # Erstellung der Karte
    fig = px.choropleth(
        df,
        geojson=counties,
        locations="fips",
        hover_name="county_name",
        color=c,
        color_continuous_scale="Thermal",
    )

    # Layout-Anpassungen für die Karte
    fig.update_geos(fitbounds="locations", visible=False)

    fig.update_layout(
        title={
            "text": c,
            "x": 0.5,
            "xanchor": "center",
            "font": {"size": 28},
        },
        coloraxis_colorbar={"title": None, "tickfont": {"size": 20}, "len": 0.75},
        margin=dict(l=1, r=1, t=50, b=1, pad=0),
    )
    fig.show()
    fig.write_image(f"map_{c}.png", "png")
