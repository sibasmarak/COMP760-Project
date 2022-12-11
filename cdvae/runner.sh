#!/bin/bash
#SBATCH --job-name=compute-recon
#SBATCH --partition=long
#SBATCH --gres=gpu:rtx8000:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=10G
#SBATCH --time=24:00:00
#SBATCH --array=0

module load anaconda/3
conda activate /home/mila/s/siba-smarak.panigrahi/.conda/envs/COMP760

# HYDRA_FULL_ERROR=1 python cdvae/run.py data=mp_20 expname=mp-cos model.predict_property=True model.kd_type=cosine

# python scripts/evaluate.py --model_path /home/mila/s/siba-smarak.panigrahi/COMP760-Project/hydra/singlerun/2022-11-23/perov-tanh --tasks recon
python scripts/compute_metrics.py --root_path /home/mila/s/siba-smarak.panigrahi/COMP760-Project/hydra/singlerun/2022-11-23/perov-l1 --tasks recon gen opt