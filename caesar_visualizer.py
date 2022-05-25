import os
import pandas as pd
import numpy as np
from vedo import *

from scipy import io
from random import choice

# pd.set_option("display.max_columns", None)
# pd.set_option("display.max_rows", None)

file_dir = './caesar/caesar-fitted-meshes'
file_list = os.listdir(file_dir)
file_name = choice(file_list)

mat_file = io.loadmat(os.path.join(file_dir,file_name))

mat_file = mat_file['points']

print(len(mat_file))
rpts = Points(mat_file, c=(0,0,0), r=5)
show(rpts, axes=1)

# for d in (0, 90, 180, 270):
#     file_name = rpts.rotateY(d)
#     file_name.show(interactive=True)