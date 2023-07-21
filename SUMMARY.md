**EndoNuke: Nuclei Detection in Endometrium Samples** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the medical industry and biomedical research. 

The dataset consists of 1780 images with 210420 labeled objects belonging to 3 different classes including *stroma*, *epithelium*, and *other nuclei*.

Images in the EndoNuke dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. There are 40 (2% of the total) unlabeled images (i.e. without annotations). There are no pre-defined <i>train/val/test</i> splits in the dataset. Alternatively, dataset could be splitted by <i>annotators</i> criteria: *ptg1* (90 images), *ptg2* (90 images), *ptg3* (88 images), *stud1* (330 images), *stud2* (684 images), *stud3* (308 images), and *stud4* (150 images). The dataset was released in 2022 by the [Institute for System Programming of the Russian Academy of Sciences (ISP RAS)](https://www.ispras.ru/en/).

Here is the visualized example grid with annotations:

<img src="https://github.com/dataset-ninja/endonuke/raw/main/visualizations/side_annotations_grid.png">
