#!/usr/bin/python3

from sys import argv
import os

def _args():
    if len(argv) != 3:
        print("Usage: python3 apply_patch.py base-dir patchs-dir")
        exit(1)

    return argv[1], argv[2]

def insert_patch(str_orig, str_search, str_insert, mode="top"):

    if mode == "top":
        position = str_orig.index(str_search)
    else:
        position = str_orig.index(str_search) + str_search.len()

    return str_orig.insert(position, str_insert)

def main():
    base_dir, patchs_dir = _args()

    files = []
    for r, _, f in os.walk(patchs_dir):
        for file in f:
            if '.patch' in file:
                files.append(os.path.join(r, file))

    for f in files:
        print("Applying " + f + " patch")

        patch_file = open(f, "r")
        patch_list = patch_file.readlines()
        patch_file.close()

        # First line of patch: original file location
        orig_file = open(base_dir + "/" + patch_list[0], "r")
        orig_list = orig_file.readlines()
        orig_file.close()

        # Second line of patch: options
        options = patch_list[1].split("")

        # Patch number of lines and mode (top or bottom), separated by a space
        patch_size = int(options[0])
        patch_mode = options[1]

        # Get patch strings
        str_insert = patch_list[2:(2+patch_size)]
        str_search = patch_list[(3+patch_size):]

        # Apply patch
        output = insert_patch(orig_list, str_search, str_insert, mode=patch_mode)

        # Write patched file
        orig_file = open(base_dir + "/" + patch_list[0], "w")
        orig_file.writelines(output)
        orig_file.close()

        print("File " + base_dir + "/" + patch_list[0] + " modified")
