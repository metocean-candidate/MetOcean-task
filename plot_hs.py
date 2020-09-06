import xarray as xr
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
import cartopy.crs as ccrs

ds = xr.open_dataset('ww3.glob_24m.202007.nc').squeeze() # File taken from the CAWCR wave hindcast
fig = plt.figure(figsize = (16,8)) # Figure size and dpi
ax = plt.axes(projection = ccrs.PlateCarree(central_longitude=180)) # Set map projection
ax.coastlines()
norm = BoundaryNorm([x/5 for x in range(0,51,1)], 256) # Define colorbar limits and spacing
pax = ax.pcolormesh(ds['longitude'], ds['latitude'], ds['hs'], norm=norm, transform=ccrs.PlateCarree())
fig.colorbar(pax, fraction=0.022, pad=0.02, ticks=[x for x in range(11)])
plt.savefig('Hs_2020_07_01T01.png',bbox_inches='tight')
