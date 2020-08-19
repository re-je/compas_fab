from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class DetectedCollisionError(Exception):
    def __init__(self, name_1, name_2):
        super(DetectedCollisionError, self).__init__()
        self.name_1 = name_1
        self.name_2 = name_2