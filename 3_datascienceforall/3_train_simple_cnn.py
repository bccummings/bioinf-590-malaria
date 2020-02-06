'''
Algorithm 3: Example from Data Science for All

Code is adapted from https://github.com/dipanjanS/data_science_for_all/blob/master/os_malaria_detection/Malaria%20Detection%20-%20Deep%20Learning%20Healthcare%20Case-Study.ipynb

Based on blog post https://towardsdatascience.com/detecting-malaria-with-deep-learning-9e45c1e34b60

Dataset used: https://lhncbc.nlm.nih.gov/publication/pub9932
'''

import os
import glob

'''
User parameters
'''
data_dir = '../data/' # location of data

'''
Segment train/validate/test
'''
base_dir = os.path.join(data_dir)
infected_dir = os.path.join(base_dir, 'Parasitized')
health_dir = os.path.join(base_dir, 'Uninfected')

infected_files = glob.glob(infected_dir+'/*.png')
healthy_files = glob.glob(infected_dir+'/*.png')


