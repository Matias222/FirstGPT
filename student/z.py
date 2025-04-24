import torch

print(torch.cuda.is_available())  # True if a CUDA-compatible GPU is available

print(torch.cuda.current_device())

device = 'cpu'
if torch.cuda.is_available():
    device = torch.cuda.current_device()

print(torch.cuda.get_device_name(0))     # GPU name

print(device)