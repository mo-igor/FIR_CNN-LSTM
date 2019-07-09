from tools import dataset
from tools.dataset import Dataset
from tools import prepare

import os
import argparse

import numpy as np


def cache_sequences(cache_dir, ):
  pass

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--dataset_dir',
      type=str,
      default=os.path.join("..", "dataset"),
      help='Path to folder containing the FIR dataset.'
  )
  parser.add_argument(
    '--model_dir',
    type=str,
    default="/"+os.path.join("tmps", "model"),
    help='Where to save the trained model.'
)
  parser.add_argument(
    '--cache_dir',
    type=str,
    default="/"+os.path.join("tmps", "cache"),
    help='Where to save the cached sequences.'
)
  parser.add_argument(
    '--epochs',
    type=int,
    default=10,
    help='How many epochs to run before ending.'
)
  parser.add_argument(
    '--frames',
    type=int,
    default=10,
    help='How many frames (time steps) in each unit.'
)
  parser.add_argument(
    '--learning_rate',
    type=float,
    default=0.01,
    help='How large a learning rate to use when training.'
)
  parser.add_argument(
    '--train_batch_size',
    type=int,
    default=100,
    help='How many images to train on at a time.'
)
  FLAGS, unparsed = parser.parse_known_args()

  data_normalized = Dataset(FLAGS.dataset_dir, minmax_normalized=True)
  prepare.sequences_by_actor(data_normalized, FLAGS.cache_dir)
