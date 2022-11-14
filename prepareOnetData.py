import torch
import pandas as pd


for split in ['train', 'val', 'test']:
    perov = pd.read_csv(f'/home/mila/s/siba-smarak.panigrahi/COMP760-Project/cdvae/data/perov_5/{split}.csv')
    print(f'Split {split}: {perov.shape}')

    onet_data = {}
    for i in perov['material_id']:
        onet_rep = torch.randn(256)
        onet_data[i] = onet_rep

    torch.save(onet_data, f'/home/mila/s/siba-smarak.panigrahi/COMP760-Project/cdvae/data/perov_5/{split}_rep.pt')