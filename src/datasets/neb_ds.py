import numpy as np
import pandas as pd

def collect_ds():
    space_ds = {
        'object': ['BHR 71', 'Horsehead Nebula', 'Orion Nebula', 'Cone Nebula', 'IC 1396', 'DR6', 'Lagoon Nebula', 'Eagle Nebula', 'IC 2944', 'Sharpless 29', 'Trifid Nebula', 'Carina Nebula', 'RCW 49'],
        'nebula_type': ['Dark Nebula', 'Dark Nebula', 'Emission Nebula', 'Dark Nebula', 'Emission Nebula', 'Emission Nebula', 'Emission Nebula', 'Emission Nebula', 'Emission Nebula', 'Emission Nebula', 'Emission Nebula', 'Emission Nebula', 'Emission Nebula'],
        'constellation': ['Musca', 'Orion', 'Orion', 'Monoceros', 'Cepheus', 'Cygnus', 'Sagittarius', 'Serpens', 'Centaurus', 'Sagittarius', 'Sagittarius', 'Carina', 'Carina'],
        'catalogue_number_1': ['BHR 71', 'Barnard 33', 'M42', 'NGC 2264', 'IC 1396', 'DR6', 'M8', 'IC 4703', 'IC 2944', 'SH 2-29', 'M20', 'NGC 3372', 'RCW 49'],
        'catalogue_number_2': [np.NAN, np.NAN, 'NGC 1976', np.NAN, np.NAN, np.NAN, 'NGC 6523', np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, 'GUM 29'],
        'distance_from_sun_ly': [600, 1500, 1500, 2500, 3000, 4000, 5200, 7000, 5900, 4100, 7600, 8000, 14000],
        'magnitude': [np.NAN, np.NAN, 4.0, 3.9, np.NAN, np.NAN, 6.0, 6.0, 4.5, 8.0, 6.3, 1.0, np.NAN]
    }
    return pd.DataFrame(space_ds)

ds_creation = collect_ds()
ds_creation.columns = ['Object', 'Nebula Type', 'Constellation', 'Catalogue Number', 'Catalogue Number 2', 'Distance from Sun (ly)', 'Magnitude']
ds_creation.to_csv('space_data.csv', index=False)
