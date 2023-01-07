import os
import shutil

if os.path.exists("build"):
    shutil.rmtree("build")
if os.path.exists("dist"):
    shutil.rmtree("dist")
if os.path.exists("serverclientmanager.egg-info"):
    shutil.rmtree("serverclientmanager.egg-info")
os.system("python setup.py sdist bdist_wheel")
os.system("twine upload --skip-existing dist/*")
