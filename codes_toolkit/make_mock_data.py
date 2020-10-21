import numpy as np

nfft = 256
n_integrations = 1000


tile_list = [1,3,4,7]
file_list = []
for i in range(4):
    for j in range(i,4):
        if i != j:
            file_list.append('X'+str(tile_list[i])+'Y'+str(tile_list[j])+'.npy')
for i in range(4):
    for j in range(i,4):
        if i != j:
            file_list.append('Y'+str(tile_list[i])+'Y'+str(tile_list[j])+'.npy')
for i in file_list:
    a = 100*(np.random.rand(nfft,n_integrations)+np.random.rand(nfft,n_integrations)*1j)
    np.save(i,a)

