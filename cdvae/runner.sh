#!/bin/bash
#SBATCH --job-name=cos-cdvae
#SBATCH --partition=long
#SBATCH --gres=gpu:rtx8000:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=10G
#SBATCH --time=12:00:00
#SBATCH --array=0

module load anaconda/3
conda activate COMP760 #/home/mila/p/prashant.govindarajan/.conda/envs/COMP760

HYDRA_FULL_ERROR=1 python cdvae/run.py data=perov_small expname=perov-small-trial model.predict_property=True model.kd_type=cosine

# python scripts/evaluate.py --model_path /home/mila/s/siba-smarak.panigrahi/COMP760-Project/hydra/singlerun/2022-11-19/perov/ --tasks gen opt
