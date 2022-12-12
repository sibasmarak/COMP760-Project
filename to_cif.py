import torch
import numpy as np
from pymatgen.core.structure import Structure
from pymatgen.analysis import energy_models as em
import pymatgen.io.cif as cif
from tqdm import tqdm 
from pymatgen.io.cif import CifWriter
from pymatgen.core.lattice import Lattice

if __name__ == '__main__':
    data = torch.load('/home/mila/p/prashant.govindarajan/scratch/COMP760-Project/cdvae/cosine/cos_eval_gen_new.pt') ## Change path
    N = data['num_atoms'].shape[1]
    j = 0
    for i in tqdm(range(N)):
        num_atoms = int(data['num_atoms'][0][i].cpu().numpy())
        lengths = tuple(data['lengths'][0][i].cpu().numpy())
        angles = tuple(data['angles'][0][i].cpu().numpy())
        lattice_params = lengths + angles
        atom_types = list(data['atom_types'][0][j:j+num_atoms].cpu().numpy())
        frac_coords = data['frac_coords'][0][j:j+num_atoms,:].cpu().numpy()
        j += num_atoms
        canonical_crystal = Structure(lattice = Lattice.from_parameters(*lattice_params),
                                    species = atom_types, coords = frac_coords, coords_are_cartesian = False)
        writer = CifWriter(canonical_crystal)
        writer.write_file('/home/mila/p/prashant.govindarajan/scratch/COMP760-Project/cdvae/cosine/generated_cifs_new/'+str(i)+'.cif')   ##Change path