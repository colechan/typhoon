import numpy as np
import netCDF4 as nc
from wrf import getvar
import sys
import os
import pandas as pd
from metpy.units import units
i = 0
data = np.zeros([20, 5], dtype=np.float)  ## Your need to mofity the "20",which represent the file numbers
df = pd.DataFrame(data, columns=['Time', 'SLP', 'MaxWind', 'lat', 'lon'])
root_dir = r'/public/home/nwpstudy/work/chenjiale/work/expr1_11/wrf/'
for file in sorted(os.listdir(root_dir)):
    if (str(file)[0:10] == 'wrfout_d01'):
        filename = root_dir + file
        print(filename)
        out = nc.Dataset(filename)
        lat = getvar(out, 'lat')
        lon = getvar(out, 'lon')
        slp = getvar(out, 'slp')
        time = getvar(out, 'XTIME')
        wind = getvar(out, 'uv10_wspd',units='kt')[0]
        q = np.where(wind == wind.max())
        k = np.where(slp == slp.min())
        df['SLP'][i] = slp[k].data
        df['MaxWind'][i] = np.array(wind[q])[0]
        df['Time'][i] = time/60
        df['lat'][i] = lat[k].data
        df['lon'][i] = lon[k].data
        i += 1
print(df)
df.to_csv("20191011_track.csv",index=False)