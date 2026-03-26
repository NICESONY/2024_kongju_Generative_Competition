from bing_image_downloader.downloader import download
import glob
import os


def extract_locations(script):
    locations = []
    tmis = []

    for line in script.split("\n"):
        if "추천 장소: " in line:
            idx = line.index("추천 장소: ") + len("추천 장소: ")
            locations.append(line[idx:].strip())
        elif "특징: " in line:
            idx = line.index("특징: ") + len("특징: ")
            tmis.append(line[idx:].strip())

    return locations, tmis


def retrieve(query_string, output_dir):
    download(
        query_string,
        limit=5,
        output_dir=os.path.join(output_dir, "dataset"),
        adult_filter_off=True,
        force_replace=False,
        timeout=60,
        verbose=True,
        filter="jpg",
    )

    dataset_dir = os.path.join(output_dir, "dataset", query_string)
    images = sorted(
        glob.glob(os.path.join(dataset_dir, "*.png"))
        + glob.glob(os.path.join(dataset_dir, "*.jpg"))
        + glob.glob(os.path.join(dataset_dir, "*.jpeg"))
    )

    if not images:
        raise FileNotFoundError(f"이미지를 찾을 수 없습니다: {dataset_dir}")
    return images[0]
