# OSVidCAP: a Framework for the Simultaneous Recognition and Description of Concurrent Actions in Videos in an Open-Set Scenario


## Introduction

Automatically understanding and describing the visual content of videos in natural language is a challenging task. Most current approaches are designed to describe single events in a closed-set setting. However, in real-world scenarios, concurrent activities and previously unseen actions may appear ina video.
The OSVidCap is a novel open-set video captioning framework that recognizes and describes, in natural language, concurrent known actions and detects the unknown ones. It is based on the encoder-decoder framework and uses a detection-and-tracking-object-based mechanism followed by a background blurring method to focus on specific targets in a video. Additionally, the TI3D Network with the Extreme Value Machine (EVM) is also used to learn representations and recognize unknown actions.


## Datasets

### LIRIS human activities dataset dataset

This repository contains proposed annotations and instructions on how to preprocess the LIRIS dataset used in the paper OSVidCap: A Framework for the Simultaneous Recognition and Description of Concurrent Actions in Videos in an Open-Set Scenario

---------------

For more information about the dataset, please see the [paper here](https://ieeexplore.ieee.org/abstract/document/9552885) 

If you use this dataset in a publication, please cite:  

A. De Souza Inácio, M. Gutoski, A. E. Lazzaretti and H. S. Lopes, "OSVidCap: A Framework for the Simultaneous Recognition and Description of Concurrent Actions in Videos in an Open-Set Scenario," in IEEE Access, vol. 9, pp. 137029-137041, 2021, doi: 10.1109/ACCESS.2021.3116882.

---------------

Videos can be downloaed from the [Liris project website](https://projet.liris.cnrs.fr/voir/activities-dataset/)


Files Information:
 - video-descriptions_known.csv    	
 	-- Contains descriptions of known actions 
 - video-descriptions_unknown.csv 
 	-- Contains descriptions of unknown actions 
 - pre_process_images_known.py
 	-- - Prepares frames of known actions from the Liris dataset.
 - pre_process_images_unknow.py
 	-- - Prepares frames of unknown actions from the Liris dataset.
 - spatial_temporal_unknown_actions.pickle
 	-- Spatial and temporal annotations of unknown actions
 - cv_1_test.txt
 	-- 1-fold cross-validation test set.
 - cv_1_train.txt
 	-- 1-fold cross-validation train set.
 - cv_2_test.txt
 	-- 2-fold cross-validation test set.
 - cv_2_train.txt
 	-- 2-fold cross-validation train set.
 - cv_3_test.txt
 	-- 3-fold cross-validation test set.
 - cv_3_train.txt
 	-- 3-fold cross-validation train set.
 - cv_4_test.txt
 	-- 4-fold cross-validation test set.
 - cv_4_train.txt
 	-- 4-fold cross-validation train set.
 - cv_5_test.txt
 	-- 5-fold cross-validation test set.
 - cv_5_train.txt
 	-- 5-fold cross-validation train set.

For more information, please contact Andrei de Souza Inacio andrei.inacioo@gmail.com

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/3.0/">Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License</a>.
