# pytorch_learn


https://www.cnblogs.com/hlikex/p/16983707.html


https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=20.04&target_type=deb_local


https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html



wget https://developer.download.nvidia.com/compute/cuda/12.6.3/local_installers/cuda_12.6.3_560.35.05_linux.run
sudo sh cuda_12.6.3_560.35.05_linux.run

## install miniconda

curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

## create d2l env

conda create --name d2l python=3.9 -y

conda activate d2l

## install torch

pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu126