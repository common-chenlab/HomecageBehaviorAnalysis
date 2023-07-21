# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 14:24:07 2023

@author: Kevin Delgado
Plot results
"""

import sys
import os
import matplotlib.pyplot as plt

import numpy as np
sys.path.append(r"Z:\Dropbox\Dropbox\Chen Lab Team Folder\Projects\Home_Cage_Training\DeepLabCut\BehaviorAnalysis\motionmapperpy")
import motionmapperpy as mmpy

def create_plot(data, animalRFID, ANIMAL_FOLDER, sigma = 0.1, c_limit=0.95):
    """ create scatter plot and heatmap for animal specific data """

    m = np.abs(data).max()

    fig, axes = plt.subplots(1, 2, figsize=(12,6))
    
    axes[0].scatter(data[:,0], data[:,1], marker='.', c=np.arange(data.shape[0]), s=1)
    axes[0].set_xlim([-m-10, m+10])
    axes[0].set_ylim([-m-10, m+10])
    axes[0].set_title(data.shape)
    
    _, xx, density = mmpy.findPointDensity(data, sigma, 511, [-m-10, m+10])
    _ = axes[1].imshow(density, cmap=mmpy.gencmap(), extent=(xx[0], xx[-1], xx[0], xx[-1]), 
              origin='lower', vmax=np.max(density)*c_limit)

    axes[1].set_title('%0.02f, %0.02f'%(sigma, c_limit))

    plot_path = os.path.join(ANIMAL_FOLDER, "HEATMAP.png")
    print("Created heatmap plot for {}!".format(animalRFID))
    fig.savefig(plot_path)