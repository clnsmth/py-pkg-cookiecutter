import os
import shutil

##############################################################################
# Utilities
##############################################################################

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


##############################################################################
# Cookiecutter clean-up
##############################################################################

no_license = "{{cookiecutter.open_source_license}}" == "None"

remove(".github/workflows/ci.yml")

# Remove license (if specified)
if no_license:
    remove("LICENSE")
