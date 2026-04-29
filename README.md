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
### Dataset Support

For each dataset, we provide a **Download Link** to facilitate integration with the toolkit.

<details>
  <summary><b>Vision Sensing</b></summary>

- CIFAR10/100 [Download Link](https://www.cs.toronto.edu/~kriz/cifar.html)
- SVHN [Download Link](http://ufldl.stanford.edu/housenumbers/)
- MNIST [Download Link](https://www.kaggle.com/datasets/hojjatk/mnist-dataset/)
- Fashion-MNIST [Download Link](https://github.com/zalandoresearch/fashion-mnist)

</details>

<details>
  <summary><b>Motion Sensing</b></summary>

- UCI HAR [Download Link](https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones)
- HHAR [Download Link](https://archive.ics.uci.edu/dataset/344/heterogeneity+activity+recognition)
- MotionSense	[Download Link](https://www.kaggle.com/datasets/malekzadeh/motionsense-dataset)
- Shoaib [Download Link](https://www.researchgate.net/publication/266384007_Sensors_Activity_Recognition_DataSet)

</details>

<details>
  <summary><b>Acoustic Sensing</b></summary>

- UrbanSound8K [Download Link](https://urbansounddataset.weebly.com/download-urbansound8k.html)
- GSC [Download Link](https://huggingface.co/datasets/google/speech_commands)
- GTZAN [Download Link](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification)
- ESC-50 [Download Link](https://github.com/karoldvl/ESC-50/archive/master.zip)

</details>

<details>
  <summary><b>Wireless Sensing</b></summary>

- Fi-Humanoid [Download Link](https://drive.google.com/drive/folders/1R0R8SlVbLI1iUFQCzh_mH90H_4CW2iwt)
- BullyDetect [Download Link](http://www.sdp8.net/Dataset?id=5ab0f5fd-a678-400a-afb2-757b2d85bc68)
- ARIL [Download Link](http://www.sdp8.net/Dataset?id=9d263468-4869-4dbb-85aa-2c63ba0a1e0f)
- UT-HAR [Download Link](https://github.com/ermongroup/Wifi_Activity_Recognition?tab=readme-ov-file)

</details>

<details>
  <summary><b>Neuromorphic Sensing</b></summary>

- CIFAR10-DVS [Download Link](https://figshare.com/articles/dataset/CIFAR10-DVS_New/4724671)
- DVS-Gesture [Download Link](https://ibm.ent.box.com/s/3hiq58ww1pbbjrinh367ykfdf60xsfm8/folder/50167556794)
- Spiking HD [Download Link](https://zenkelab.org/resources/spiking-heidelberg-datasets-shd/)
- Spiking SC [Download Link](https://zenkelab.org/resources/spiking-heidelberg-datasets-shd/)

</details>

---

### Spike-Wise Encoding Methods

For each encoding method, we provide its **Original Reference** to facilitate reproducibility and proper academic attribution.

- Rate coding [Research Link](https://ieeexplore.ieee.org/abstract/document/10242251)
- Time-to-first-spike (TTFS) coding [Research Link](https://ieeexplore.ieee.org/abstract/document/10242251)
- Burst coding [Research Link](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2021.638474/full)
- Phase coding [Research Link](https://ieeexplore.ieee.org/abstract/document/10502282)
- Temporal-switch (TS) coding [Research Link](https://link.springer.com/chapter/10.1007/978-3-030-58607-2_23)

---
### LIF-Based Neuron Variants

For each lif-based neuron variant, we provide its **Original Reference** to facilitate reproducibility.

- GLIF [Research Link](https://proceedings.neurips.cc/paper_files/paper/2022/hash/cfa8440d500a6a6867157dfd4eaff66e-Abstract-Conference.html)
- INTLIF [Research Link](https://link.springer.com/chapter/10.1007/978-3-031-73411-3_15)
- PSN [Research Link](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a834ac3dfdb90da54292c2c932c997cc-Abstract-Conference.html)
- TLIF [Research Link](https://ojs.aaai.org/index.php/AAAI/article/view/29114)
- PLIF [Research Link](http://openaccess.thecvf.com/content/ICCV2021/html/Fang_Incorporating_Learnable_Membrane_Time_Constant_To_Enhance_Learning_of_Spiking_ICCV_2021_paper.html)
- CLIF [Research Link](https://arxiv.org/abs/2402.04663)
- ILIF [Research Link](https://arxiv.org/abs/2505.10371)
- RPLIF [Research Link](https://dl.acm.org/doi/abs/10.1145/3746027.3755030)

---
### Architectures for Spiking Neural Networks

For each architecture, we provide its **Original Reference** to facilitate reproducibility and proper academic attribution.

- SpikingVGG [Research Link](https://www.ijcai.org/proceedings/2024/0596.pdf)
- SEW-ResNet [Research Link](https://proceedings.neurips.cc/paper/2021/hash/afe434653a898da20044041262b3ac74-Abstract.html)
- MS-ResNet [Research Link](https://ieeexplore.ieee.org/abstract/document/10428029)
- Spikformer [Research Link](https://arxiv.org/abs/2209.15425)
- Meta-Spikeformer [Research Link](https://arxiv.org/abs/2404.03663)
- QKFormer [Research Link](https://proceedings.neurips.cc/paper_files/paper/2024/hash/179f5dcdeedc149443ebd3ba70811dbd-Abstract-Conference.html)
- SpikingResFormer [Research Link](http://openaccess.thecvf.com/content/CVPR2024/html/Shi_SpikingResformer_Bridging_ResNet_and_Vision_Transformer_in_Spiking_Neural_Networks_CVPR_2024_paper.html)

---
### Acknowledgement

We gratefully acknowledge [SpikingJelly](https://github.com/fangwei123456/spikingjelly)
 and [snnTorch](https://github.com/jeshraghian/snntorch)
, which provide key ideas and foundational components for this repository.
