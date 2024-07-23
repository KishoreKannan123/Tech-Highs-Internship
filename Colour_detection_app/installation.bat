python -m pip install --upgrade pip setuptools virtualenv
python -m venv kivy_venv
call kivy_venv\Scripts\activate.bat
python -m pip install "kivy[base]" kivy_examples
pip install opencv-python
pip install pandas
pip install numpy
