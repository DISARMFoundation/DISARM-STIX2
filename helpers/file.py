import json
import os
from stix2 import Bundle
import shutil


def write_disarm_dir(dir):
    """

     Args:
        dir (str): a directory name

    Returns:

    """
    try:
        os.mkdir('output/')
    except FileExistsError:
        pass

    try:
        os.mkdir('output/' + dir)
    except FileExistsError:
        pass


def clean_output_dir():
    """Recursively delete the output folder.

    Returns:

    """
    shutil.rmtree("output/")


def write_file(file_name, file_data):
    """Write a JSON file to ./output.

    Args:
        file_name (str): a file name
        file_data (str): the file json data

    Returns:

    """
    with open(file_name, 'w') as f:
        # f.write(json.dumps(file_data, sort_keys=True, indent=4))
        f.write(file_data.serialize(pretty=True))
        f.write('\n')


def write_files(stix_objects):
    """

    Args:
        stix_objects:

    Returns:

    """
    for i in stix_objects:
        write_disarm_dir(i.type)
        write_file(f"output/{i.type}/{i.id}.json", Bundle(i, allow_custom=True))


def write_bundle(bundle, bundle_name):
    """

    Args:
        bundle:
        bundle_name:

    Returns:

    """
    write_file(f"output/{bundle_name}.json", bundle)
