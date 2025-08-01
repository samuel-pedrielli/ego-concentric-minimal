import torch
import torch.nn.functional as F

def identity_loss(a_t, a_tp1, a_tp1_upper=None, alpha=1.0, gamma=1.0):
    """Geometric placeholder; replace with model‑specific operators."""
    lid = alpha * F.mse_loss(a_tp1, a_t)
    if a_tp1_upper is not None:
        lid = lid + gamma * F.mse_loss(a_tp1, a_tp1_upper)
    return lid

def welfare_loss(ca, h):
    """L_welfare(h,a) = ||C(a) - h||^2 (placeholder)."""
    return F.mse_loss(ca, h)
