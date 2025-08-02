import os
import pandas as pd
import numpy as np

sample = os.listdir()

def read_list_of_csv(thing) -> list[np.ndarray]:
    result = []
    for i in thing:
        if i.startswith("tem.rawdata"):
            tem_array = pd.read_csv(i)
            tem_array = tem_array.iloc[0:100, 0:5].astype(np.float32)
            result.append(tem_array.to_numpy())
    return np.stack(result)

save = read_list_of_csv(sample)
# For later use

import h5py as hp
# This code saves the numpy array to an HDF5 file which acts like a multidimensional array
# and can be used for efficient storage and retrieval of large datasets

with hp.File('tem_data.h5', 'w') as h5f: # Write mode
    h5f.create_dataset('tem_array', data=save)

with hp.File('tem_data.h5', 'r') as h5f: # Read mode
    loaded = h5f['tem_array'][:]
    print(f"Loaded data shape: {loaded.shape}")

with hp.File('tem_data.h5', 'r') as h5f: # Read mode
    print(loaded)

