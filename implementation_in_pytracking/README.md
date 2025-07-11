# Anti-UAV410 Dataset Integration with PyTracking

This guide provides step-by-step instructions to evaluate and train trackers using the [Anti-UAV410](https://drive.google.com/file/d/1zsdazmKS3mHaEZWS2BnqbYHPEcIaH5WR/view?usp=sharing) dataset within the [PyTracking](https://github.com/visionml/pytracking) framework.

## Prerequisites

- Download and install the [PyTracking repository](https://github.com/visionml/pytracking) along with its corresponding environment.

---

## 🧪 Evaluation on the Anti-UAV410 Dataset

### 1. Add Dataset Loader
Download `ForTesting/antiuav410dataset.py` and place it into:

```shell
pytracking_project/pytracking/evaluation/
```


### 2. Register Dataset in `datasets.py`
Edit `pytracking/pytracking/evaluation/datasets.py` and add the following lines:

```python
antiuav410_test=DatasetInfo(module=pt % "antiuav410", class_name="AntiUAV410Dataset", kwargs=dict(split='test')),
antiuav410_val=DatasetInfo(module=pt % "antiuav410", class_name="AntiUAV410Dataset", kwargs=dict(split='val')),
```

### 3. Add Dataset Path in `local.py`
Edit `pytracking/pytracking/evaluation/local.py` and add:

```python
settings.antiuav410_path = '/media/share/data2/TrackingDatasets/Anti-UAV410/'
```

### 4. Run Evaluation Using AntoUAV410

Test set:
```bash
python pytracking/run_tracker.py tomp tomp50 --dataset_name antiuav410_test
```
Validation set:
```bash
python pytracking/run_tracker.py tomp tomp50 --dataset_name antiuav410_val
```


## 🏋️‍♂️ Training on the Anti-UAV410 Dataset

### 1. Add Dataset Loader
Download `ForTraining/antiuav410.py` and place it into:

```shell
pytracking_project/ltr/dataset/
```

### 2. Register Dataset Module
Edit `pytracking_project/ltr/dataset/__init__.py` and add the following line:

```python
from .antiuav410 import AntiUAV410
```

### 3. Add Dataset Path
Edit `pytracking_project/ltr/admin/local.py` and add the following line:

```python
self.antiuav410_dir = '/media/data2/TrackingDatasets/Anti-UAV410/'
```

### 4. Configure Training Script
Edit `pytracking_project/ltr/train_settings/tomp/tomp50.py` and configure training and validation datasets:

```python
from ltr.dataset import AntiUAV410
```

```python
    # Train datasets
    antiuav410_train = AntiUAV410(settings.env.antiuav410_dir, split='train')
    # lasot_train = Lasot(settings.env.lasot_dir, split='train')
    # got10k_train = Got10k(settings.env.got10k_dir, split='vottrain')
    # trackingnet_train = TrackingNet(settings.env.trackingnet_dir, set_ids=list(range(4)))
    # coco_train = MSCOCOSeq(settings.env.coco_dir)

    # Validation datasets
    antiuav410_val = AntiUAV410(settings.env.antiuav410_dir, split='val')
    # got10k_val = Got10k(settings.env.got10k_dir, split='votval')
```
```python
    # Train sampler and loader
    # dataset_train = sampler.DiMPSampler([lasot_train, got10k_train, trackingnet_train, coco_train], [1, 1, 1, 1],
    #                                     samples_per_epoch=settings.train_samples_per_epoch, max_gap=settings.max_gap,
    #                                     num_test_frames=settings.num_test_frames, num_train_frames=settings.num_train_frames,
    #                                     processing=data_processing_train)

    dataset_train = sampler.DiMPSampler([antiuav410_train], [1],
                                        samples_per_epoch=settings.train_samples_per_epoch, max_gap=settings.max_gap,
                                        num_test_frames=settings.num_test_frames, num_train_frames=settings.num_train_frames,
                                        processing=data_processing_train)

    loader_train = LTRLoader('train', dataset_train, training=True, batch_size=settings.batch_size, num_workers=settings.num_workers,
                             shuffle=True, drop_last=True, stack_dim=1)

    # Validation samplers and loaders
    # dataset_val = sampler.DiMPSampler([got10k_val], [1], samples_per_epoch=settings.val_samples_per_epoch,
    #                                   max_gap=settings.max_gap, num_test_frames=settings.num_test_frames,
    #                                   num_train_frames=settings.num_train_frames, processing=data_processing_val)
    dataset_val = sampler.DiMPSampler([antiuav410_val], [1], samples_per_epoch=settings.val_samples_per_epoch,
                                      max_gap=settings.max_gap, num_test_frames=settings.num_test_frames,
                                      num_train_frames=settings.num_train_frames, processing=data_processing_val)

    loader_val = LTRLoader('val', dataset_val, training=False, batch_size=settings.batch_size, num_workers=settings.num_workers,
                           shuffle=False, drop_last=True, epoch_interval=settings.val_epoch_interval, stack_dim=1)
```

### 5. Run Training
```bash
python ltr/run_training.py tomp tomp50
```


## 📁 Directory Overview
```bash
pytracking/
├── pytracking/
│   └── evaluation/
│       ├── antiuav410dataset.py         # dataset loader for evaluation
│       ├── datasets.py                  # register dataset
│       └── local.py                     # set dataset path
├── ltr/
│   ├── dataset/
│   │   ├── __init__.py                  # dataset loader for evaluation
│   │   └── antiuav410.py                # dataset loader for training
│   ├── train_settings/
│   │   └── tomp/tomp50.py              # training config
│   ├── admin/local.py                  # set training dataset path
└── ...
```

## 📌 Notes

- You can quickly set up Anti-UAV410 by directly replacing the corresponding files in the PyTracking project with those found under the `ForTesting/` and `ForTraining/` directories.

- You can train and evaluate a variety of trackers depending on your needs, such as **TaMOs**, **RTS**, **ToMP**, **KeepTrack**, **LWL**, **KYS**, **PrDiMP**, **DiMP**, and **ATOM** trackers.
