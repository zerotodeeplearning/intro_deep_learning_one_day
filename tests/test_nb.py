import subprocess
import tempfile
import os

# d = "solutions_do_not_open/"
d = "labs"

def _exec_notebook(fname):
    path = os.path.join(d, fname)
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=1000",
                "--output", fout.name, path]
        subprocess.check_call(args)



def test_01():
    _exec_notebook("Lab_01_Jupyter_Numpy_Matplotlib.ipynb")

def test_02():
    _exec_notebook("Lab_02_Keras_Shallow_Models.ipynb")

def test_03():
    _exec_notebook("Lab_03_Keras_Fully_Connected_Models.ipynb")

def test_04():
    _exec_notebook("Lab_04_Tensorflow_2.0.ipynb")
