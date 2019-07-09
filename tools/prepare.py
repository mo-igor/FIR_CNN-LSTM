import os
from tqdm import tqdm 

import numpy as np

def ensure_structure_exist(dir_list):
    """Makes sure the folder exists on disk.

    Args:
    dir_list: List of path strings.
    """
    for dir_name in dir_list:
        ensure_dir_exists(dir_name)

def ensure_dir_exists(dir_name):
    """Makes sure the folder exists on disk.

    Args:
    dir_name: Path to the folder.
    """
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

def sequences_by_actor(dataset, cache_dir):
    samples_dir = os.path.join(cache_dir, "samples")
    if os.path.exists(samples_dir):
        print("[INFO] Removing {}...".format(samples_dir))
    ensure_dir_exists(samples_dir)
    print("[INFO] Adding samples to {}...".format(samples_dir))
    for actor in dataset.actors:
        ensure_dir_exists(os.path.join(samples_dir, actor))
    for sample in tqdm(dataset):
        name = sample.sequence_name.split(".")[0]
        for action in sample.annotation():
            start, stop, label, actor = action
            stop += 1
            fn = label + "_" + name + "_" + str(start) + "_" + str(stop) + ".npy"
            path = os.path.join(samples_dir, actor, fn)
            with open(path, 'wb+') as handler:
                np.save(handler, action, allow_pickle=False)
                handler.flush()

    pass 