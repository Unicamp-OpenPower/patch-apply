# Patch apply

## Requirements:
- python3

## Usage:
  ```./apply_patch.py base-dir patchs-dir```
  
- `base-dir` is the base source code directory to apply the patchs
- `patchs-dir` is the directory with the `.patch` files
  
 ## Patch files
 - `.patch` extension.
 - First line: relative location of the source file to apply the patch
 - Second line: number of lines of the patch AND top OR bottom (position of the patch relative to the search string)
 - Patch lines
 - 1 line separation
 - Search string on the original source file
