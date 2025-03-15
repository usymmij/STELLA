# make sure to run variables.sh first

cd carla_garage/team_code

CUDA_VISIBLE_DEVICES=0 OMP_NUM_THREADS=8 OPENBLAS_NUM_THREADS=1 torchrun --nnodes=1 --nproc_per_node=1 --max_restarts=0 train.py --id model_2 --batch_size 4 --setting all --root_dir /mnt/scratch/stella/carla_garage/data/ --logdir /mnt/scratch/saves/ --cpu_cores 8 --use_controller_input_prediction 1 --continue_epoch 0 --load_file /mnt/scratch/saves/model_1/model_0030_0.pth
