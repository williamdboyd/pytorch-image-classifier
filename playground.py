import torch
import numpy as np

data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x_data = torch.tensor(data)

np_array = np.array(data)
x_np = torch.from_numpy(np_array)

print(f"Tensor: \n {x_data} \n")
print(f"NumPy tensor: \n {x_np}")

rand_tensor = torch.rand(3, 3, 3)

print(f"Random tensor: \n {rand_tensor} \n")