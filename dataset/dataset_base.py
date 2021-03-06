"""Small library that points to a data set.

Methods of Data class:
  data_files: Returns a python list of all (sharded) data set files.
  num_examples_per_epoch: Returns the number of examples in the data set.
  num_classes: Returns the number of classes in the data set.
  reader: Return a reader for a single entry from the data set.
"""

from abc import ABCMeta
from abc import abstractmethod
import tensorflow as tf


class Dataset(object):
    """A simple class for handling data sets."""
    __metaclass__ = ABCMeta

    def __init__(self, name, subset):
        """Initialize dataset using a subset and the path to the data."""
        assert subset in self.available_subsets(), self.available_subsets()
        self.name = name
        self.subset = subset

    @abstractmethod
    def num_classes(self):
        """Returns the number of classes in the data set."""
        pass
        # return 10

    @abstractmethod
    def num_examples_per_epoch(self):
        """Returns the number of examples in the data subset."""
        pass

    @abstractmethod
    def data_files(self):
        """Returns a python list of all (sharded) data subset files.

          Returns:
            python list of all (sharded) data set files.
        Raises:
          ValueError: if there are not data_files matching the subset.
        """
        pass

    def available_subsets(self):
        """Returns the list of available subsets."""
        return ['train', 'val']

    def reader(self):
        """Return a reader for a single entry from the data set.

        See io_ops.py for details of Reader class.

        Returns:
          Reader object that reads the data set.
        """
        return tf.TFRecordReader()
