from setuptools import setup, find_packages

setup(
    name='simple_elmo',
    version='0.0.1',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples', 'test']),
    install_requires=[
        "pandas",
        "scikit-learn",
        "h5py",
        "numpy",
        "tensorflow=1.15.2",
        "smart_open>1.8.1",
    ],
)