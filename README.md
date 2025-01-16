# pytorch_learn


https://www.cnblogs.com/hlikex/p/16983707.html


https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=20.04&target_type=deb_local


https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html

## 安装cuda流程记录

### 关闭 nouveau

https://blog.csdn.net/u012229282/article/details/124442555

sudo vim /etc/modprobe.d/blacklist-nouveau.conf

添加
blacklist nouveau
options nouveau modeset=0

更新initramfs

sudo update-initramfs -u

sudo reboot

查看nouveau是否被禁用

### 安装cuda

wget https://developer.download.nvidia.com/compute/cuda/12.6.3/local_installers/cuda_12.6.3_560.35.05_linux.run
sudo sh cuda_12.6.3_560.35.05_linux.run

### install miniconda

curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

### create d2l env

conda create --name d2l python=3.9 -y

conda activate d2l

### install torch

pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu126

### install d2l

pip install d2l==1.0.3

