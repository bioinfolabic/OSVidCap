# OSVidCAP: a Framework for the Simultaneous Recognition and Description of Concurrent Actions in Videos in an Open-Set Scenario


## Introduction

Automatically understanding and describing the visual content of videos in natural language is a challenging task. Most current approaches are designed to describe single events in a closed-set setting. However, in real-world scenarios, concurrent activities and previously unseen actions may appear ina video.
The OSVidCap is a novel open-set video captioning framework that recognizes and describes, in natural language, concurrent known actions and detects the unknown ones. It is based on the encoder-decoder framework and uses a detection-and-tracking-object-based mechanism followed by a background blurring method to focus on specific targets in a video. Additionally, the TI3D Network with the Extreme Value Machine (EVM) is also used to learn representations and recognize unknown actions.


## Dataset description

In our experiments, we use the LIRIS human activities dataset. It was designed for recognizing complex and realistic actions in videos and made availablefor the ICPR-HARL 2012 competition. The full dataset contains 828 actions (including discussing, telephone calls, givingan item, etc.) performed by 21 different people in 10 differentclasses. It was organized into two independent subsets: the D1 subset, with depth and grayscale images, and the D2 subset, with color images. The dataset also has unannotated actions, such as walking, running, whiteboard writing,book leafing, etc. In this study, we used the D2 subset that contains 367 annotated actions from 167 videos. Each action consists of one or more people performing one or more different activities. Besides, 116 video segments in 15 different unannotated actions were extracted from the original videos. They were considered as unknown activities. Each new video segment was also annotated with spatial, temporal, and description information.

Videos are available on the Liris human activity [website](https://projet.liris.cnrs.fr/voir/activities-dataset/download.html) 



![Known Action histograms](known_actions.png)

![Unknown Action histograms](unknown_actions.png)




## Related Papers

If you use of thisse datasets, please cite the following reference in any publications:

A. De Souza Inácio, M. Gutoski, A. E. Lazzaretti and H. S. Lopes, "OSVidCap: A Framework for the Simultaneous Recognition and Description of Concurrent Actions in Videos in an Open-Set Scenario," in IEEE Access, vol. 9, pp. 137029-137041, 2021, doi: 10.1109/ACCESS.2021.3116882.


```
@ARTICLE{9552885,
  author={De Souza Inácio, Andrei and Gutoski, Matheus and Lazzaretti, André Eugênio and Lopes, Heitor Silvério},
  journal={IEEE Access}, 
  title={OSVidCap: A Framework for the Simultaneous Recognition and Description of Concurrent Actions in Videos in an Open-Set Scenario}, 
  year={2021},
  volume={9},
  number={},
  pages={137029-137041},
  doi={10.1109/ACCESS.2021.3116882}}

```
* The LIRIS human activities dataset

C Wolf, J. Mille, E. Lombardi, O. Celiktutan, M. Jiu, E. Dogan, G. Eren, M. Baccouche, E. Dellandrea, C.-E. Bichot, C. Garcia, B. Sankur, Evaluation of video activity localizations integrating quality and quantity measurements, In Computer Vision and Image Understanding (127):14-30, 2014.

