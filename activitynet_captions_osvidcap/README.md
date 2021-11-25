# OSVidCAP: a Framework for the Simultaneous Recognition and Description of Concurrent Actions in Videos in an Open-Set Scenario


## Introduction

Automatically understanding and describing the visual content of videos in natural language is a challenging task. Most current approaches are designed to describe single events in a closed-set setting. However, in real-world scenarios, concurrent activities and previously unseen actions may appear ina video.
The OSVidCap is a novel open-set video captioning framework that recognizes and describes, in natural language, concurrent known actions and detects the unknown ones. It is based on the encoder-decoder framework and uses a detection-and-tracking-object-based mechanism followed by a background blurring method to focus on specific targets in a video. Additionally, the TI3D Network with the Extreme Value Machine (EVM) is also used to learn representations and recognize unknown actions.


## Datasets

### ActivityNet Captions dataset

This repository contains instructions on how to download and preprocessing the dataset used in the paper OSVidCap: A Framework for the Simultaneous Recognition and Description of Concurrent Actions in Videos in an Open-Set Scenario

----------------

For more information about the dataset, please see the [paper here](https://ieeexplore.ieee.org/abstract/document/9552885) 

If you use this dataset in a publication, please cite:  

A. De Souza Inácio, M. Gutoski, A. E. Lazzaretti and H. S. Lopes, "OSVidCap: A Framework for the Simultaneous Recognition and Description of Concurrent Actions in Videos in an Open-Set Scenario," in IEEE Access, vol. 9, pp. 137029-137041, 2021, doi: 10.1109/ACCESS.2021.3116882.



Files Information:
 - download_videos.py    	
 	-- Dataset downloading code 
 - ids_train.txt
 - ids_val.txt 
 	-- Contains video ids for training and validation set 
 - video-descriptions_cleaned_train.csv
 - video-descriptions_cleaned_val.csv
 	-- - Contains descriptions of known actions 
 - video-descriptions_unknown_train_X.csv
 - video-descriptions_unknown_val_X.csv
 - video-descriptions_unknown_test_X.csv
 	-- 5-fold cross-validation train and test set.

For more information, please contact Andrei de Souza Inacio andrei.inacioo@gmail.com
