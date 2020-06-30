# -*- coding: utf-8 -*-
"""
Created on Mon Jun  15 17:01:00 2020

@author: LEANDRO
"""
from oversampling.os import OS
import numpy as np


from oversampling.core import estimation
from oversampling.core import generation

class O2PF_RI(OS):
    
	def variant(self, X, generate_n):
		clf, cluster2samples = self.run(X)
		return self.computeVariant(clf, cluster2samples, X, generate_n,estimation.mean_gaussian,generation.geometric_euclidean)
