import torch

@torch.no_grad()
def identity_stability(a_t, a_tT):
    diff = torch.norm(a_tT - a_t) ** 2
    return torch.exp(-diff)
