import os
from random import choice
from scipy import io
import numpy as np

np.set_printoptions(threshold=np.inf)

file_dir = './caesar/caesar'
# file_dir = './caesar/caesar-fitted-meshes'

if file_dir.endswith('meshes'):
    file_list = os.listdir(file_dir)
    file_name = choice(file_list)
    mat_file = io.loadmat(os.path.join(file_dir,file_name))
    
    # print(mat_file.keys()) # caesar file has __header__, __version__, __globals__, points
    print(f"name :          {file_name}")
    print(f"header  :       {mat_file['__header__']}")
    print(f"version :       {mat_file['__version__']}")
    print(f"globals :       {mat_file['__globals__']}") # empty
    print(f"n_points :      {len(mat_file['points'])}") # numpy array

else: #evaluation case
    file_name = 'landmarksIdxs73.mat'
    mat_file = io.loadmat(os.path.join(file_dir,file_name))

    print(mat_file.keys()) # caesar file has __header__, __version__, __globals__, evalues
    # print(f"name :          {file_name}")
    # print(f"header  :       {mat_file['__header__']}")
    # print(f"version :       {mat_file['__version__']}")
    # print(f"globals :       {mat_file['__globals__']}") # empty
    # print(f"n_points :      {mat_file['landmarksIdxs']}") # numpy array