import os

files = []


def get_files(source_dir, ext="jpg"):
    for entry in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, entry)):
            file_name = os.path.join(source_dir, entry)
            if file_name.split(".")[-1].lower() == ext.lower():
                files.append(file_name)

        elif os.path.isdir(os.path.join(source_dir, entry)):
            sub_dir = os.path.join(source_dir, entry)
            get_files(sub_dir)


def getChildIdsFromPath(path, ext="jpg"):
    global files
    files = []
    get_files(path, ext)
    all_ids = []
    for file in files:
        child_id = rf"{file}".split("\\")[-1].split("_")[0]
        all_ids.append(str(child_id))
    return all_ids