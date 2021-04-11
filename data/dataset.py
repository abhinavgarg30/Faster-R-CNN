from .voc_dataset import VOCBboxDataset
from .utils import preprocess, Transform


class Dataset:
    def __init__(self, opt):
        self.opt = opt
        self.db = VOCBboxDataset(opt.voc_data_dir)
        self.tsf = Transform(opt.min_size, opt.max_size)

    def __getitem__(self, idx):
        ori_img, bbox, label = self.db[idx]
        img, bbox, label, scale = self.tsf((ori_img, bbox, label))
        return img.copy(), bbox.copy(), label.copy(), scale

    def __len__(self):
        return len(self.db)


class TestDataset:
    def __init__(self, opt, split='test'):
        self.opt = opt
        self.db = VOCBboxDataset(opt.voc_data_dir, split=split)

    def __getitem__(self, idx):
        ori_img, bbox, label = self.db[idx]
        img = preprocess(ori_img)
        return img, ori_img.shape[1:], bbox, label

    def __len__(self):
        return len(self.db)
