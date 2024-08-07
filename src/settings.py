from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME = "EndoNuke"
PROJECT_NAME_FULL = "EndoNuke: Nuclei Detection in Endometrium Samples"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_4_0()
INDUSTRIES: List[Industry] = [Industry.Medical()]
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Medical(), Research.Biomedical()]
CATEGORY: Category = Category.Medical()

CV_TASKS: List[CVTask] = [
    CVTask.InstanceSegmentation(),
    CVTask.SemanticSegmentation(),
    CVTask.ObjectDetection(),
]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.InstanceSegmentation()]

RELEASE_DATE: Optional[str] = "2022-06-01"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://endonuke.ispras.ru/"

PREVIEW_IMAGE_ID: int = 16562530

GITHUB_URL: str = "https://github.com/dataset-ninja/endonuke"

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = "https://www.ispras.ru/conf/endonuke/data.zip"

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = "https://www.mdpi.com/2306-5729/7/6/75"
CITATION_URL: Optional[str] = "https://www.mdpi.com/2306-5729/7/6/75"
AUTHORS: Optional[List[str]] = [
    "Anton Naumov",
    "Andrey Ivanov",
    "Egor Ushakov",
    "Evgeny Karpulevich",
    "Tatiana Khovanskaya",
    "Alexandra Konyukova",
    "Konstantin Midiber",
    "Nikita Rybak",
    "Maria Ponomareva",
    "Alesya Lesko",
    "Ekaterina Volkova",
    "Polina Vishnyakova",
    "Sergey Nora",
    "Liudmila Mikhaleva",
    "Timur Fatkhudinov",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = (
    "Institute for System Programming of the Russian Academy of Sciences (ISP RAS)"
)
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://www.ispras.ru/en/"

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = {
    "annotators": "annotator",
}
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME, PROJECT_NAME_FULL]
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "hide_dataset": HIDE_DATASET,        
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
