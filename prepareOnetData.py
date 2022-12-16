import torch
import pandas as pd
import pickle


for split in ['test']:
    perov = pd.read_csv(f'/home/mila/s/siba-smarak.panigrahi/COMP760-Project/cdvae/data/perov_5/{split}.csv')
    print(f'Split {split}: {perov.shape}')

    onet_data = {}
    for i in perov['material_id']:
        onet_rep = torch.randn(256)
        onet_data[i] = onet_rep

    pickle.dump(onet_data, open(f'/home/mila/s/siba-smarak.panigrahi/COMP760-Project/cdvae/data/perov_5/{split}_rep.pkl', 'wb'))