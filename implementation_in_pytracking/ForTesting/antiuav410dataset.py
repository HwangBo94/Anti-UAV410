import os
import numpy as np
import glob
import os.path as osp
import json
from pytracking.evaluation.data import Sequence, BaseDataset, SequenceList
from pytracking.utils.load_text import load_text
from PIL import Image
from pathlib import Path


class AntiUAV410Dataset(BaseDataset):
    """
    AntiUAV410 dataset.

    """

    def __init__(self, split):
        super().__init__()
        if split == 'test' or split == 'val':
            self.base_path = os.path.join(self.env_settings.antiuav410_path, split)
        else:
            self.base_path = os.path.join(self.env_settings.antiuav410_path, 'train')
        # image and annotation paths
        anno_files = sorted(glob.glob(os.path.join(self.base_path,
                                                        '*/IR_label.json')))
        seq_dirs = [osp.dirname(f) for f in anno_files]
        seq_names = [osp.basename(d) for d in seq_dirs]

        self.sequence_list = seq_names
        
        self.split = split

    def get_sequence_list(self):
        return SequenceList([self._construct_sequence(s) for s in self.sequence_list])

    def _construct_sequence(self, sequence_name):

        # import pdb;pdb.set_trace()
        anno_path = '{}/{}/IR_label.json'.format(self.base_path, sequence_name)

        with open(anno_path, 'r') as f:

            ground_truth_rect=json.load(f)['gt_rect']
            ground_truth_rect=np.array(ground_truth_rect,dtype=np.float64)


        frames_path = '{}/{}'.format(self.base_path, sequence_name)
        frame_list = [frame for frame in os.listdir(frames_path) if frame.endswith('.jpg')]
        frame_list.sort(key=lambda f: int(f[:-4]))
        frames_list = [os.path.join(frames_path, frame) for frame in frame_list]

        return Sequence(sequence_name, frames_list, 'antiuav410', ground_truth_rect.reshape(-1, 4))

    def __len__(self):
        return len(self.sequence_list)

