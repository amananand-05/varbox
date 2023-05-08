from setuptools import setup
import setuptools

setup(
    name='varbox',
    version='2.0',
    description='varbox package can be used to dump and load multiple variables through local file and can also be used as encryption vault',
    author= 'Aman Anand',
    author_email='amananandofficials@gmail.com',
    keywords=['varbox dump', 'varbox load', 'varbox pickle load', 'varbox pickle dump','varbox','variable dump','encryption',"encryptor"],
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.8.8',
    py_modules=['cipher','varbox'],
    package_dir={'':'varbox'},
    packages=['constants','encryption','varboxexceptions'],
    install_requires = [
        "pycryptodome==3.17"
    ],
    include_package_data=True,
    zip_safe=False
)


# python setup.py bdist_wheel 
# pip install -e . 
# python setup.py sdist  
# python setup.py bdist_wheel sdist
# twine upload dist/*   

