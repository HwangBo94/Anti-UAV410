# PyTracking
A general python framework for visual object tracking and video object segmentation, based on **PyTorch**.

### :fire: One tracking paper accepted at WACV 2024! 👇
* [Beyond SOT: Tracking Multiple Generic Objects at Once](https://arxiv.org/abs/2212.11920) | **Code available!**


### :fire: One tracking paper accepted at WACV 2023! 👇
* [Efficient Visual Tracking with Exemplar Transformers](https://arxiv.org/abs/2112.09686) | **Code available!**

### :fire: One tracking paper accepted at ECCV 2022! 👇
* [Robust Visual Tracking by Segmentation](https://arxiv.org/abs/2203.11191) | **Code available!**


## Highlights

### TaMOs, RTS, ToMP, KeepTrack, LWL, KYS, PrDiMP, DiMP and ATOM Trackers

Official implementation of the **TaMOs** (WACV  2024), **RTS** (ECCV 2022), **ToMP** (CVPR 2022), **KeepTrack** (ICCV 2021), **LWL** (ECCV 2020), **KYS** (ECCV 2020), **PrDiMP** (CVPR 2020),
**DiMP** (ICCV 2019), and **ATOM** (CVPR 2019) trackers, including complete **training code** and trained models.

### [Tracking Libraries](pytracking)

Libraries for implementing and evaluating visual trackers. It includes

* All common **tracking** and **video object segmentation** datasets.  
* Scripts to **analyse** tracker performance and obtain standard performance scores.
* General building blocks, including **deep networks**, **optimization**, **feature extraction** and utilities for **correlation filter** tracking.  

### [Training Framework: LTR](ltr)
 
**LTR** (Learning Tracking Representations) is a general framework for training your visual tracking networks. It is equipped with

* All common **training datasets** for visual object tracking and segmentation.  
* Functions for data **sampling**, **processing** etc.  
* Network **modules** for visual tracking.
* And much more...


### [Model Zoo](MODEL_ZOO.md)
The tracker models trained using PyTracking, along with their results on standard tracking 
benchmarks are provided in the [model zoo](MODEL_ZOO.md). 


## Trackers
The toolkit contains the implementation of the following trackers.

### TaMOs (WACV 2024)

**[[Paper]](https://arxiv.org/abs/2212.11920) [[Raw results]](MODEL_ZOO.md#Raw-Results-1)
[[Models]](MODEL_ZOO.md#Models-1) [[Training Code]](./ltr/README.md#TaMOs)  [[Tracker Code]](./pytracking/README.md#TaMOs)**

Official implementation of **TaMOs**. TaMOs is the first generico object tracker to tackle the problem of tracking multiple
generic object at once. It uses a shared model predictor consisting of a Transformer in order to produce multiple
target models (one for each specified target). It achieves sub-linear run-time when tracking multiple objects and
outperforms existing single object trackers when running one instance for each target separately.
TaMOs serves as the baseline tracker for the new large-scale generic object tracking  benchmark LaGOT  (see [here](https://github.com/google-research-datasets/LaGOT))
that contains multiple annotated target objects per sequence.

![TaMOs_teaser_figure](pytracking/.figs/TaMOs_overview.png)

### RTS (ECCV 2022)

**[[Paper]](https://arxiv.org/abs/2203.11191) [[Raw results]](MODEL_ZOO.md#Raw-Results-1)
[[Models]](MODEL_ZOO.md#Models-1) [[Training Code]](./ltr/README.md#RTS)  [[Tracker Code]](./pytracking/README.md#RTS)**

Official implementation of **RTS**. RTS is a robust, end-to-end trainable, segmentation-centric pipeline that internally
works with segmentation masks instead of bounding boxes. Thus, it can learn a better target representation that clearly
differentiates the target from the background. To achieve the necessary robustness for challenging tracking scenarios,
a separate instance localization component is used to condition the segmentation decoder when producing the output mask.

![RTS_teaser_figure](pytracking/.figs/rts_overview.png)

### ToMP (CVPR 2022)

**[[Paper]](https://arxiv.org/abs/2203.11192) [[Raw results]](MODEL_ZOO.md#Raw-Results-1)
  [[Models]](MODEL_ZOO.md#Models-1) [[Training Code]](./ltr/README.md#ToMP)  [[Tracker Code]](./pytracking/README.md#ToMP)**

Official implementation of **ToMP**. ToMP employs a Transformer-based 
model prediction module in order to localize the target. The model predictor is further extended to estimate a second set
of weights that are applied for accurate bounding box regression.
The resulting tracker ToMP relies on training and on test frame information in order to predict all weights transductively.

![ToMP_teaser_figure](pytracking/.figs/ToMP_teaser.png)

### KeepTrack (ICCV 2021)

**[[Paper]](https://arxiv.org/abs/2103.16556)  [[Raw results]](MODEL_ZOO.md#Raw-Results-1)
  [[Models]](MODEL_ZOO.md#Models-1)  [[Training Code]](./ltr/README.md#KeepTrack)  [[Tracker Code]](./pytracking/README.md#KeepTrack)**

Official implementation of **KeepTrack**. KeepTrack actively handles distractor objects to
continue tracking the target. It employs a learned target candidate association network, that
allows to propagate the identities of all target candidates from frame-to-frame.
To tackle the problem of lacking groundtruth correspondences between distractor objects in visual tracking,
it uses a training strategy that combines partial annotations with self-supervision. 

![KeepTrack_teaser_figure](pytracking/.figs/KeepTrack_teaser.png)


### LWL (ECCV 2020)
**[[Paper]](https://arxiv.org/pdf/2003.11540.pdf)  [[Raw results]](MODEL_ZOO.md#Raw-Results-1)
  [[Models]](MODEL_ZOO.md#Models-1)  [[Training Code]](./ltr/README.md#LWL)  [[Tracker Code]](./pytracking/README.md#LWL)**
    
Official implementation of the **LWL** tracker. LWL is an end-to-end trainable video object segmentation architecture
which captures the current target object information in a compact parametric
model. It integrates a differentiable few-shot learner module, which predicts the
target model parameters using the first frame annotation. The learner is designed
to explicitly optimize an error between target model prediction and a ground
truth label. LWL further learns the ground-truth labels used by the
few-shot learner to train the target model. All modules in the architecture are trained end-to-end by maximizing segmentation accuracy on annotated VOS videos. 

![LWL overview figure](pytracking/.figs/lwtl_overview.png)

### KYS (ECCV 2020)
**[[Paper]](https://arxiv.org/pdf/2003.11014.pdf)  [[Raw results]](MODEL_ZOO.md#Raw-Results)
  [[Models]](MODEL_ZOO.md#Models)  [[Training Code]](./ltr/README.md#KYS)  [[Tracker Code]](./pytracking/README.md#KYS)**
    
Official implementation of the **KYS** tracker. Unlike conventional frame-by-frame detection based tracking, KYS 
propagates valuable scene information through the sequence. This information is used to
achieve an improved scene-aware target prediction in each frame. The scene information is represented using a dense 
set of localized state vectors. These state vectors are propagated through the sequence and combined with the appearance
model output to localize the target. The network is learned to effectively utilize the scene information by directly maximizing tracking performance on video segments
![KYS overview figure](pytracking/.figs/kys_overview.png)

### PrDiMP (CVPR 2020)
**[[Paper]](https://arxiv.org/pdf/2003.12565)  [[Raw results]](MODEL_ZOO.md#Raw-Results)
  [[Models]](MODEL_ZOO.md#Models)  [[Training Code]](./ltr/README.md#PrDiMP)  [[Tracker Code]](./pytracking/README.md#DiMP)**
    
Official implementation of the **PrDiMP** tracker. This work proposes a general 
formulation for probabilistic regression, which is then applied to visual tracking in the DiMP framework.
The network predicts the conditional probability density of the target state given an input image.
The probability density is flexibly parametrized by the neural network itself.
The regression network is trained by directly minimizing the Kullback-Leibler divergence. 

### DiMP (ICCV 2019)
**[[Paper]](https://arxiv.org/pdf/1904.07220)  [[Raw results]](MODEL_ZOO.md#Raw-Results)
  [[Models]](MODEL_ZOO.md#Models)  [[Training Code]](./ltr/README.md#DiMP)  [[Tracker Code]](./pytracking/README.md#DiMP)**
    
Official implementation of the **DiMP** tracker. DiMP is an end-to-end tracking architecture, capable
of fully exploiting both target and background appearance
information for target model prediction. It is based on a target model prediction network, which is derived from a discriminative
learning loss by applying an iterative optimization procedure. The model prediction network employs a steepest descent 
based methodology that computes an optimal step length in each iteration to provide fast convergence. The model predictor also
includes an initializer network that efficiently provides an initial estimate of the model weights.  

![DiMP overview figure](pytracking/.figs/dimp_overview.png)
 
### ATOM (CVPR 2019)
**[[Paper]](https://arxiv.org/pdf/1811.07628)  [[Raw results]](MODEL_ZOO.md#Raw-Results)
  [[Models]](MODEL_ZOO.md#Models)  [[Training Code]](./ltr/README.md#ATOM)  [[Tracker Code]](./pytracking/README.md#ATOM)**  
 
Official implementation of the **ATOM** tracker. ATOM is based on 
(i) a **target estimation** module that is trained offline, and (ii) **target classification** module that is 
trained online. The target estimation module is trained to predict the intersection-over-union (IoU) overlap 
between the target and a bounding box estimate. The target classification module is learned online using dedicated 
optimization techniques to discriminate between the target object and background.
 
![ATOM overview figure](pytracking/.figs/atom_overview.png)
 
### ECO/UPDT (CVPR 2017/ECCV 2018)
**[[Paper]](https://arxiv.org/pdf/1611.09224.pdf)  [[Models]](https://drive.google.com/open?id=1aWC4waLv_te-BULoy0k-n_zS-ONms21S)  [[Tracker Code]](./pytracking/README.md#ECO)**  

An unofficial implementation of the **ECO** tracker. It is implemented based on an extensive and general library for [complex operations](pytracking/libs/complex.py) and [Fourier tools](pytracking/libs/fourier.py). The implementation differs from the version used in the original paper in a few important aspects. 
1. This implementation uses features from vgg-m layer 1 and resnet18 residual block 3.   
2. As in our later [UPDT tracker](https://arxiv.org/pdf/1804.06833.pdf), seperate filters are trained for shallow and deep features, and extensive data augmentation is employed in the first frame.  
3. The GMM memory module is not implemented, instead the raw projected samples are stored.  

Please refer to the [official implementation of ECO](https://github.com/martin-danelljan/ECO) if you are looking to reproduce the results in the ECO paper or download the raw results.

## Associated trackers
We list associated trackers that can be found in external repositories.  

### E.T.Track (WACV 2023)

**[[Paper]](https://arxiv.org/abs/2112.09686) [[Code]](https://github.com/pblatter/ettrack)**

Official implementation of **E.T.Track**. E.T.Track utilized our proposed Exemplar Transformer, a transformer module 
utilizing a single instance level attention layer for realtime visual object tracking. E.T.Track is up to 8x faster than 
other transformer-based models, and consistently outperforms competing lightweight trackers that can operate in realtime 
on standard CPUs. 

![ETTrack_teaser_figure](pytracking/.figs/ETTrack_overview.png)

## Installation

#### Clone the GIT repository.  
```bash
git clone https://github.com/visionml/pytracking.git
```
   
#### Clone the submodules.  
In the repository directory, run the commands:  
```bash
git submodule update --init  
```  
#### Install dependencies
Run the installation script to install all the dependencies. You need to provide the conda install path (e.g. ~/anaconda3) and the name for the created conda environment (here ```pytracking```).  
```bash
bash install.sh conda_install_path pytracking
```  
This script will also download the default networks and set-up the environment.  

**Note:** The install script has been tested on an Ubuntu 18.04 system. In case of issues, check the [detailed installation instructions](INSTALL.md). 

**Windows:** (NOT Recommended!) Check [these installation instructions](INSTALL_win.md). 

#### Let's test it!
Activate the conda environment and run the script pytracking/run_webcam.py to run ATOM using the webcam input.  
```bash
conda activate pytracking
cd pytracking
python run_webcam.py dimp dimp50    
```  


## What's next?

#### [pytracking](pytracking) - for implementing your tracker

#### [ltr](ltr) - for training your tracker

## Contributors

### Main Contributors
* [Martin Danelljan](https://martin-danelljan.github.io/)  
* [Goutam Bhat](https://goutamgmb.github.io/)
* [Christoph Mayer](https://2006pmach.github.io/)
* [Matthieu Paul](https://github.com/mattpfr)

### Guest Contributors
* [Felix Järemo-Lawin](https://liu.se/en/employee/felja34) [LWL]

## Acknowledgments
* Thanks for the great [PreciseRoIPooling](https://github.com/vacancy/PreciseRoIPooling) module.  
* We use the implementation of the Lovász-Softmax loss from https://github.com/bermanmaxim/LovaszSoftmax.  
