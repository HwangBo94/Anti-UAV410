from __future__ import absolute_import

import unittest
import os

from trackers.SiamFC.siamfc import TrackerSiamFC
from experiments import ExperimentAntiUAV410


dataset_path='D:/Codes/Datasets/Anti-UAV410/Anti-UAV410/Anti-UAV/'

# test or val
subset='test'

net_path = './Trackers/SiamFC/model.pth'
tracker = TrackerSiamFC(net_path=net_path)

# run experiment
experiment = ExperimentAntiUAV410(root_dir=dataset_path, subset=subset)

experiment.run(tracker, visualize=True)
# report performance
experiment.report([tracker.name])