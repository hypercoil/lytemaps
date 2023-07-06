# `minnmaps`

This repository contains an implementation of a minimal subset of `neuromaps` functionality. If you're an end user, this is likely not for you -- this implementation exists mostly for developer purposes. As developers, we'd sometimes like to use certain `neuromaps` operations without burdening our software with the bulky dependencies (`nilearn`, `sklearn` and Connectome Workbench) that the full install of `neuromaps` requires. This implementation is intended to support the subset of functionality that requires only core Scientific Python packages together with the essential `nibabel` and `requests`. Obviously, functionality here is limited. As development progresses, we'll index the `neuromaps` functions that are implemented below.

If you use this repository, please follow the citation prescriptions from [Neuromaps](https://github.com/netneurolab/neuromaps) and [nilearn](https://github.com/nilearn/nilearn)

### License

Most code in this repository is taken directly from the `neuromaps` repository, and is therefore licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License. The exception to this is several functions in `minnmaps/utils.py` and `minnmaps/datasets/utils.py`, which are taken from the `nilearn` and `sklearn` repositories and are therefore licensed under the 3-clause BSD license. See the `LICENSE` file for more details.
