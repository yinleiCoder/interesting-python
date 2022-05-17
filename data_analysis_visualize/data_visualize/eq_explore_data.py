import json
import plotly.express as px
import pandas as pd

filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))
mags = []# 震级
titles = []
lons, lats = [], [] # 经纬度
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lat = eq_dict['geometry']['coordinates'][0]
    lon = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lats.append(lat)
    lons.append(lon)
print(mags[:10])
print(titles[:10])
print(lats[:10])
print(lons[:10])

data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级']
)
fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置',
    # x=lons,
    # y=lats,
    # labels={"x": "lon", "y": "lat"},
    # range_x=[-200, 200],
    # range_y=[-90, 90],
    # width=800,
    # height=800,
    # title='global earthquakes',
)
fig.write_html('global_earthquakes.html')
fig.show()

# Express中可用的渐变
for key in px.colors.named_colorscales():
    print(key)