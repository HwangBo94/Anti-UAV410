# Anti-UAV410 Benchmark

Anti-UAV410: A Thermal Infrared Benchmark and Customized Scheme for Tracking Drones in the Wild

This toolkit is used to evaluate trackers on generalized infrared UAV tracking benchmark called Anti-UAV410. The benchmark comprises a total of 410 videos with over 438K manually annotated bounding boxes.

## Preparing the dataset
Download the Anti-UAV410 dataset ([Google drive](https://drive.google.com/file/d/1zsdazmKS3mHaEZWS2BnqbYHPEcIaH5WR/view?usp=sharing) and [Baidu disk](https://pan.baidu.com/s/1R-L9gKIRowMgjjt52n48-g?pwd=a410) Access code: a410) to your disk, the organized directory should look like:

    ```
    --AntiUAV410/
    	|--test
    	|--train
    	|--val
    ```


## Installation and testing
**Step 1.** Create a conda environment and activate it.

```shell
conda create -n AntiUAV410 python=3.9.12
conda activate AntiUAV410
```

**Step 2.** Install the requirements.
```shell
pip install opencv-python, matplotlib, wget, shapely

pip install torch===1.9.1 -f https://download.pytorch.org/whl/torch_stable.html
pip install torchvision===0.10.1 -f https://download.pytorch.org/whl/torch_stable.html
```
Other versions of python, cuda and torch are also compatible.

**Step 3.** Testing the default SiamFC tracker.

Change the dataset_path in the Demo_for_tracking.py file to the path where the dataset is located.

Run
```shell
python Demo_for_tracking.py
```
The tracking results will be saved at project_dir/results/AntiUAV410/test/SiamFC.

**Step 4.** Downloading the tracking results compared in the paper.

Download the tracking results ([Google drive](https://drive.google.com/file/d/1zaNOoGZ2zXf-z3QoffgcH2W8HNxyR0kA/view?usp=sharing) and [Baidu disk](https://pan.baidu.com/s/169Gu_iDSVEBqu9Wz2hQA0g?pwd=a410) Access code: a410) to your project directory, the organized directory should look like:

    ```
    --project_dir/tracking_results/
    	|--Defaults
    	|--Trained_with_antiuav410
    ```

The files inside the Defaults directory are the results of the trackers that are not trained with Anti-UAV410 dataset, while The files inside the Trained_with_antiuav410 directory are the results of the trackers that are re-trained with Anti-UAV410 dataset.

**Step 5.** Visual comparison.

Change the dataset path and select the trackers that need to be compared visually.

Run
```shell
python Demo_for_visual_comparison.py
```

The comparison figures will be saved at project_dir/figures/.
<!---
![contents](./figures/02_6319_1500-2999.jpg)
-->
<img src="figures/02_6319_1500-2999.jpg" width="30%"><img src="figures/3700000000002_144152_1.jpg" width="30%"><img src="figures/3700000000002_152538_1.jpg" width="30%">


``not exist'' in the figure means that the target is occluded or out of view.

**Step 6.** Evaluating the trackers.

Change the dataset path and edit project_dir/utils/trackers.py to select the trackers to be evaluated.

Run
```shell
python Evaluation_for_ALL.py
```

The evaluation plots will be saved at project_dir/reports/AntiUAV410/.

Over 50 trackers are involved, they are:
### Default trackers

<img src="reports/AntiUAV410/test/precision_plots.png" width="48%"><img src="reports/AntiUAV410/test/success_plots.png" width="48%">

* **MixFormerV2-B.** Cui, Yutao, et al. "Mixformerv2: Efficient fully transformer tracking." NIPS, 2023. [[Github]](https://github.com/MCG-NJU/MixFormerV2)
* **ROMTrack.** Cai, Yidong, et al. "Robust object modeling for visual tracking." ICCV, 2023. [[Github]](https://github.com/dawnyc/ROMTrack)
* **GRM.**  Gao, Shenyuan, et al. "Generalized relation modeling for transformer tracking." CVPR, 2023. [[Github]](https://github.com/Little-Podi/GRM)
* **DropTrack.**  Wu, Qiangqiang, et al. "Dropmae: Masked autoencoders with spatial-attention dropout for tracking tasks." CVPR, 2023. [[Github]](https://github.com/jimmy-dq/DropMAE)
* **ARTrack.**  Wei, Xing, et al. "Autoregressive visual tracking." CVPR, 2023. [[Github]](https://github.com/MIV-XJTU/ARTrack)
* **SeqTrack-B256.**  Chen, Xin, et al. "Seqtrack: Sequence to sequence learning for visual object tracking." CVPR, 2023. [[Github]](https://github.com/microsoft/VideoX)
* **SeqTrack-B384.**  Chen, Xin, et al. "Seqtrack: Sequence to sequence learning for visual object tracking." CVPR, 2023. [[Github]](https://github.com/microsoft/VideoX)



SeqTrack-B256 [66] CVPR23 52.87 56.38
SeqTrack-B384 [66] CVPR23 49.97 53.01
JointNLT [65] CVPR23 48.92 54.36
SwinTrack-Tiny [64] NIPS22 51.23 56.83
SwinTrack-Base [64] NIPS22 52.41 55.76
ToMP50 [63] CVPR22 52.95 55.56
ToMP101 [63] CVPR22 54.52 60.14
TCTrack [62] CVPR22 35.37 35.05
SLT-TransT [61] ECCV22 50.90 57.62
OSTrack-256 [60] ECCV22 43.75 52.60
OSTrack-384 [60] ECCV22 53.53 59.20
AiATrack [59] ECCV22 53.91 55.24
Unicorn-Large [58] ECCV22 56.55 59.38
Unicorn-Tiny [58] ECCV22 55.42 58.93
RTS [57] ECCV22 54.68 57.19
KeepTrack [56] ICCV21 55.97 58.34
Stark-ST50 [55] ICCV21 54.07 61.43
Stark-ST101 [55] ICCV21 54.15 59.57
HiFT [54] ICCV21 33.84 41.74
STMTrack [53] CVPR21 38.98 41.24
TrDiMP [51] CVPR21 50.20 55.47
TransT [52] CVPR21 48.85 55.24
ROAM [50] CVPR20 42.41 47.77
Siam R-CNN [12] CVPR20 60.54 64.81
SiamBAN [38] CVPR20 36.69 38.36
SiamCAR [39] CVPR20 41.73 48.18
GlobalTrack [42] AAAI20 59.34 63.39
KYS [49] ECCV20 44.70 49.61
Super DiMP [48] - 53.12 55.87
PrDiMP50 [47] CVPR20 51.87 53.35
SiamFC++ [46] AAAI20 41.03 45.15































### Re-trained trackers


## Citation

If you find this project useful in your research, please consider cite:

```latex
@article{huang2023anti,
  title={Anti-UAV410: A Thermal Infrared Benchmark and Customized Scheme for Tracking Drones in the Wild},
  author={Huang, Bo and Li, Jianan and Chen, Junjie and Wang, Gang and Zhao, Jian and Xu, Tingfa},
  journal={IEEE Transactions on Pattern Analysis and Machine Intelligence},
  year={2023},
  publisher={IEEE}
}
```
