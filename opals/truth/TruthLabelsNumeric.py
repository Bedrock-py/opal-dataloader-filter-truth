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
import os

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

    # naive, needs improvement
    def check(self, name, col):
        return True

    # writes the truth labels to a separate file
    def apply(self, conf):
        labels = list(set(conf['values']))
        keys = [labels.index(x) for x in conf['values']]
        if not os.path.exists(conf['storepath']):
            os.makedirs(conf['storepath'])
        with open(conf['storepath'] + 'truth_labels.csv', 'w') as labelsFile:
            line = ','.join([str(x) for x in keys])
            labelsFile.write(line)
        return None

