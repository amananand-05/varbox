installation steps: 

python setup.py bdist_wheel 
pip install -e . 
python setup.py sdist  
python setup.py bdist_wheel sdist
twine upload dist/*   