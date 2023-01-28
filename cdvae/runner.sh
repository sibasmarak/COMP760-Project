#!/bin/bash
#SBATCH --job-name=cdvae-mp20-eval
#SBATCH --partition=long
#SBATCH --gres=gpu:rtx8000:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=48:00:00
#SBATCH --array=0

module load anaconda/3
conda activate cdvae #/home/mila/p/prashant.govindarajan/.conda/envs/COMP760
wandb login 3323892d9a4991ee28c9d175976b0b8a921dcf37
# HYDRA_FULL_ERROR=1 python cdvae/run.py data=mp_20 expname=mp-bravais model.predict_property=True 
# HYDRA_FULL_ERROR=1 python cdvae/run.py data=perov_super expname=cdvaedummy model.predict_property=True

python scripts/evaluate.py --model_path /home/mila/p/prashant.govindarajan/scratch/COMP760-Project/hydra/singlerun/2023-01-25/mp-bravais --tasks recon gen opt --num_batches_to_samples 5
python scripts/compute_metrics.py --root_path /home/mila/p/prashant.govindarajan/scratch/COMP760-Project/hydra/singlerun/2023-01-25/mp-bravais --tasks recon gen opt