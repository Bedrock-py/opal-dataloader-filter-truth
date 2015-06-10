#****************************************************************
# Copyright (c) 2015, Georgia Tech Research Institute
# All rights reserved.
#
# This unpublished material is the property of the Georgia Tech
# Research Institute and is protected under copyright law.
# The methods and techniques described herein are considered
# trade secrets and/or confidential. Reproduction or distribution,
# in whole or in part, is forbidden except by the express written
# permission of the Georgia Tech Research Institute.
#****************************************************************/

from dataloader.utils import *
import time
import numpy as np
from sklearn import preprocessing

class TruthLabelsNumeric(Filter):
    def __init__(self):
        super(TruthLabelsNumeric, self).__init__()
        self.name = 'TruthLabels'
        self.description = 'Extracts the truth labels.'
        self.type = 'extract'
        self.stage = 'after'
        self.input = 'Numeric'
        self.outputs = ['truth_labels.csv']
        self.parameters_spec = []
        self.possible_names = ['class','truth']

    def check(self, name, col):
        return True

    def apply(self, conf):
        #sets everything to a 0-n scale, even if starting at 1
        labels = list(set(conf['values']))
        keys = [labels.index(x) for x in conf['values']]
        with open(conf['storepath'] + 'truth_labels.csv', 'w') as labelsFile:
            line = ','.join([str(x) for x in keys])
            labelsFile.write(line)
        return None

