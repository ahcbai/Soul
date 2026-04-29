This repository is maintained anonymously for the paper submitted to NeurIPS 2026, entitled “A Comprehensive Benchmark for Edge Sensing Workloads with Spiking Neural Networks”. It provides the code and resources used in our experimental evaluation.

This project provides implementations and benchmarks of representative SNN neuron models and network algorithms up to the end of 2025, serving as a **versioned snapshot of the current methodological landscape**.

> Methods released in 2026 are explicitly considered out-of-scope for this release, as the benchmark is intended to be a **curated and fixed evaluation suite rather than a continuously expanding collection**.
While we acknowledge that new methods will continue to emerge, incorporating them requires a§§ separate curation and validation cycle to ensure fairness and consistency of comparison.
We plan to periodically update the benchmark in future releases, with a dedicated 2026 update covering representative methods introduced during that year.

### Usage

You can run the library on a single GPU from the command line:

```bash
CUDA_VISIBLE_DEVICES=[GPU_ID] python run_soul.py \
    -dataset=[DATASET_NAME] \
    -data_dir=[DATASET_DIRECTORY] \
    -T=[NUM_TIMESTEPS] \
    -m=[MODEL_NAME] \
    -n=[NEURON_TYPE] \
    -seed=[SEED_NUMBER]
```

We provide all experimental commands described in the paper in the `scripts` directory for reproducibility.

**Any use, reproduction, or distribution of this code without prior written permission from the authors is strictly prohibited.**

---

- CIFAR10/100 [Download Link]()

---

### Acknowledgement

We gratefully acknowledge [SpikingJelly](https://github.com/fangwei123456/spikingjelly)
 and [snnTorch](https://github.com/jeshraghian/snntorch)
, which provide key ideas and foundational components for this repository.
