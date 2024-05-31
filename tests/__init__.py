import sys
import os

project_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_dir)

# this sys.path.append step is not needed if you run in a Repo, or in a Git folder with DBR 14.3+
# this sys.path.append step is needed if you run the test locally, in the Github action, in the cluster terminal, or in older DBR versions.
