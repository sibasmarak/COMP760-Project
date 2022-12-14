#!/bin/bash
#SBATCH --job-name=cdvae-eval
#SBATCH --partition=long
#SBATCH --gres=gpu:rtx8000:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=48:00:00
#SBATCH --array=0

module load anaconda/3
conda activate COMP760 #/home/mila/p/prashant.govindarajan/.conda/envs/COMP760

# HYDRA_FULL_ERROR=1 python cdvae/run.py data=mp_20 expname=mp-cos model.predict_property=True model.kd_type=cosine
# HYDRA_FULL_ERROR=1 python cdvae/run.py data=perov_super expname=cdvaedummy model.predict_property=True

python scripts/evaluate.py --model_path /home/mila/s/siba-smarak.panigrahi/COMP760-Project/hydra/singlerun/2022-12-15/cdvae-ptr-128-correct --tasks recon gen opt --num_batches_to_samples 5
python scripts/compute_metrics.py --root_path /home/mila/s/siba-smarak.panigrahi/COMP760-Project/hydra/singlerun/2022-12-15/cdvae-ptr-128-correct --tasks recon gen opt