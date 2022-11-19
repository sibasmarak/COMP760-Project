#!/bin/bash
#SBATCH --job-name=cdvae
#SBATCH --partition=long
#SBATCH --gres=gpu:rtx8000:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=10G
#SBATCH --time=24:00:00
#SBATCH --array=0

module load anaconda/3
conda activate /home/mila/s/siba-smarak.panigrahi/.conda/envs/COMP760

HYDRA_FULL_ERROR=1 python cdvae/run.py data=perov expname=perov