import torch
import pandas as pd
import pickle
from tqdm import tqdm


for split in ['train', 'val', 'test']:
    perov = pd.read_csv(f'/home/mila/s/siba-smarak.panigrahi/COMP760-Project/cdvae/data/mp_20/{split}.csv')
    print(f'Split {split}: {perov.shape}')

    onet_data = {}
    for i in tqdm(perov['material_id']):
        onet_rep = torch.randn(256)
        onet_data[i] = onet_rep

    pickle.dump(onet_data, open(f'/home/mila/s/siba-smarak.panigrahi/COMP760-Project/cdvae/data/mp_20/{split}_rep.pkl', 'wb'))