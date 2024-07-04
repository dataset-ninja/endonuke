**EndoNuke: Nuclei Detection in Endometrium Samples** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the medical industry, and in the biomedical research. 

The dataset consists of 1780 images with 215758 labeled objects belonging to 3 different classes including *stroma*, *epithelium*, and *other nuclei*.

Images in the EndoNuke dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. All images are labeled (i.e. with annotations). There are no pre-defined <i>train/val/test</i> splits in the dataset. Alternatively, the dataset could be split into 7 annotators: ***stud2*** (90456 instances), ***stud1*** (37797 instances), ***stud3*** (37655 instances), ***ptg2*** (16297 instances), ***stud4*** (13480 instances), ***ptg1*** (11649 instances), and ***ptg3*** (8424 instances). The dataset was released in 2022 by the <span style="font-weight: 600; color: grey; border-bottom: 1px dashed #d3d3d3;">Institute for System Programming of the Russian Academy of Sciences (ISP RAS)</span>.

<img src="https://github.com/dataset-ninja/endonuke/raw/main/visualizations/poster.png">
