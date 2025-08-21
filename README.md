“Deprecated — replaced by ego-centric-agi”

# Concentric EGO — Minimal Experiment (skeleton)

Small, clean starting point to explore an **identity regularizer** (`L_id`) and an **identity–welfare coupling** (`L_welfare`) on instruction‑tuned LLMs.

> Status: skeleton only. Define your task, plug the losses, and run A0/A1/A2.

## Arms
- **A0**: baseline task training
- **A1**: baseline + `L_id`
- **A2**: baseline + `L_id + L_welfare`

## Metrics (to define)
- Identity stability `S_id(T)`
- Robustness under prompt attacks
- Downstream alignment metric of your choice

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m experiments.run_minimal
```

## References
- EA Forum post: https://forum.effectivealtruism.org/posts/eh2XPCXguyjw3LAg3/ego-centric-architecture-for-agi-safety-technical-core
- One‑pager: https://samuel-pedrielli.github.io/assets/OnePager_EGO-AGI.pdf

## Roadmap
- [ ] Define pass/fail criteria
- [ ] Minimal notebook with A0/A1/A2
- [ ] Small ablation
