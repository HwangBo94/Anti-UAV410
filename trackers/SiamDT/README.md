# This is the official implementation of SiamDT



## Installation
**Step 1.** Create a conda environment and activate it.

```shell
conda create -n SiamDT python=3.7
conda activate SiamDT
```

**Step 2.** Install torch, torchvision.
```shell
pip install torch===1.8.1+cu111 -f https://download.pytorch.org/whl/torch_stable.html
pip install torchvision===0.9.1+cu111 -f https://download.pytorch.org/whl/torch_stable.html
```
Other versions of python, cuda and torch are also compatible. Please refer to the installation requirements for SwinTransformer, [swin](https://github.com/SwinTransformer/Swin-Transformer-Object-Detection)

**Step 3.** Install mmcv-full.
```shell
pip install -U openmim
mim install mmcv-full==1.3.0 -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.8.1/index.html
```

**Step 4.** Install other requirements.
```shell
pip install matplotlib opencv-python shapely visdom
```

**Step 5.** Build Swin Transformer Object Detection.
```shell
cd libs/swintransformer/
pip install -r requirements/build.txt
python setup.py develop
```

**Step 6.** Preparing pre-trained models.

Download the pre-trained model at the [Swin Transformer project](https://github.com/SwinTransformer/Swin-Transformer-Object-Detection), this tutorial uses Cascade Mask R-CNN framework and Swin-T backbone as an example.

1) Download 'cascade_mask_rcnn_swin_tiny_patch4_window7.pth' at this [link](https://objects.githubusercontent.com/github-production-release-asset-2e65be/357198522/73ea3400-9bd5-11eb-83e7-331b886c412d?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240501%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240501T162023Z&X-Amz-Expires=300&X-Amz-Signature=91248b1d595dccb8dda2ed8367940cd1eead343f6c36e8d471f26b3fe571b055&X-Amz-SignedHeaders=host&actor_id=89343149&key_id=0&repo_id=357198522&response-content-disposition=attachment%3B%20filename%3Dcascade_mask_rcnn_swin_tiny_patch4_window7.pth&response-content-type=application%2Foctet-stream)

2) Run 'utils/obtain_pretrained_weights.py' to get the weights for backbone and neck, and save it as a tar file for compatibility with lower versions of torch.

3) Place the 'cascade_mask_rcnn_swin_tiny.pth.tar' generated in step 2) under the 'SiamDT/pretrained_weights/' folder path.

Note: Or you can download the processed pre-trained weights from this link.

**Step 7.** Train SiamDT.

Change the dataset path in 'datasets/wrappers.py' and run:
```shell
python tracking_train_demo.py
```

**Step 8.** Test SiamDT.

Change the dataset path in 'tracking_test_demo.py':
```shell
python tracking_test_demo.py
```

Note: If you want to visualise the tracking results, please use the following command first:
```shell
python -m visdom.server -port=5123
```
Then you can then see the visualisation on the [http://localhost:5123/](http://localhost:5123/).
