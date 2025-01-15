import torch
from torch import nn
from d2l import torch as d2l

def cpu():  #@save
    """Get the CPU device."""
    return torch.device('cpu')

def gpu(i=0):  #@save
    """Get a GPU device."""
    return torch.device(f'cuda:{i}')

print (cpu(), gpu(), gpu(1))

def num_gpus():  #@save
    """Get the number of available GPUs."""
    return torch.cuda.device_count()

print (num_gpus())

def try_gpu(i=0):  #@save
    """Return gpu(i) if exists, otherwise return cpu()."""
    if num_gpus() >= i + 1:
        return gpu(i)
    return cpu()

def try_all_gpus():  #@save
    """Return all available GPUs, or [cpu(),] if no GPU exists."""
    return [gpu(i) for i in range(num_gpus())]

print (try_gpu(), try_gpu(10), try_all_gpus())