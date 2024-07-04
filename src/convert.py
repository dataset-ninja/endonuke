# # https://endonuke.ispras.ru/

import glob
import os

import supervisely as sly
from supervisely.io.fs import get_file_name
from tqdm import tqdm

# project_name = "ENDONUKE"
dataset_path = "/mnt/d/datasetninja-raw/endonuke/data/dataset"
ds_name = "ds0"
# batch_size = 30


def convert_and_upload_supervisely_project(api, workspace_id, project_name):

    def _create_ann(image_path):
        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        image_name = get_file_name(image_path)
        ann_path = ann_name_to_data.get(get_file_name(image_name))
        if ann_path is None:
            return sly.Annotation(img_size=(image_np.shape[0], image_np.shape[1]))
        labels = []
        curr_meta_folder = ann_path.split("/")[-2]
        curr_tag_meta = folder_to_tag_meta[curr_meta_folder]
        tag = sly.Tag(curr_tag_meta)

        with open(ann_path) as f:
            content = f.read().split("\n")

        for curr_point_str in content:
            if len(curr_point_str) != 0:
                curr_point = list(map(int, curr_point_str.split(" ")))
                point = sly.Point(curr_point[1], curr_point[0])
                label = sly.Label(point, index_to_class[curr_point[2]])
                labels.append(label)

        return sly.Annotation(
            img_size=(image_np.shape[0], image_np.shape[1]), labels=labels, img_tags=[tag]
        )

    images_path = os.path.join(dataset_path, "images")
    images_names = os.listdir(images_path)
    annotation_path = os.path.join(dataset_path, "labels")

    obj_class_stroma = sly.ObjClass("stroma", sly.Point, color=[15, 105, 138])
    obj_class_epithelium = sly.ObjClass("epithelium", sly.Point, color=[208, 2, 27])
    obj_class_other_nuclei = sly.ObjClass("other nuclei", sly.Point, color=[138, 37, 15])
    index_to_class = {0: obj_class_stroma, 1: obj_class_epithelium, 2: obj_class_other_nuclei}

    tag_meta_ptg1 = sly.TagMeta("ptg1", sly.TagValueType.NONE, sly.TagApplicableTo.IMAGES_ONLY)
    tag_meta_ptg2 = sly.TagMeta("ptg2", sly.TagValueType.NONE, sly.TagApplicableTo.IMAGES_ONLY)
    tag_meta_ptg3 = sly.TagMeta("ptg3", sly.TagValueType.NONE, sly.TagApplicableTo.IMAGES_ONLY)
    tag_meta_stud1 = sly.TagMeta("stud1", sly.TagValueType.NONE, sly.TagApplicableTo.IMAGES_ONLY)
    tag_meta_stud2 = sly.TagMeta("stud2", sly.TagValueType.NONE, sly.TagApplicableTo.IMAGES_ONLY)
    tag_meta_stud3 = sly.TagMeta("stud3", sly.TagValueType.NONE, sly.TagApplicableTo.IMAGES_ONLY)
    tag_meta_stud4 = sly.TagMeta("stud4", sly.TagValueType.NONE, sly.TagApplicableTo.IMAGES_ONLY)

    folder_to_tag_meta = {
        "ptg1": tag_meta_ptg1,
        "ptg2": tag_meta_ptg2,
        "ptg3": tag_meta_ptg3,
        "stud1": tag_meta_stud1,
        "stud2": tag_meta_stud2,
        "stud3": tag_meta_stud3,
        "stud4": tag_meta_stud4,
    }

    tag_metas = sly.TagMetaCollection(
        [
            tag_meta_ptg1,
            tag_meta_ptg2,
            tag_meta_ptg3,
            tag_meta_stud1,
            tag_meta_stud2,
            tag_meta_stud3,
            tag_meta_stud4,
        ]
    )

    project = api.project.create(workspace_id, project_name)

    obj_class_collection = sly.ObjClassCollection(
        [obj_class_stroma, obj_class_epithelium, obj_class_other_nuclei]
    )
    meta = sly.ProjectMeta(obj_classes=obj_class_collection, tag_metas=tag_metas)
    api.project.update_meta(project.id, meta.to_json())

    dataset = api.dataset.create(project.id, ds_name)

    bulk_anns = glob.glob(annotation_path + "/*/*/*.txt")

    ann_name_to_data = {}

    for curr_ann_path in bulk_anns:
        ann_name = get_file_name(curr_ann_path)
        ann_name_to_data[ann_name] = curr_ann_path

    progress = tqdm(desc=f"Create dataset {ds_name}", total=len(images_names))

    for images_names_batch in sly.batched(images_names):
        img_pathes_batch = [
            os.path.join(images_path, image_name) for image_name in images_names_batch
        ]

        anns_batch = [_create_ann(image_path) for image_path in img_pathes_batch]

        img_infos = api.image.upload_paths(dataset.id, images_names_batch, img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        api.annotation.upload_anns(img_ids, anns_batch)

        progress.update(len(images_names_batch))
