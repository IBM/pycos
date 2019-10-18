from setuptools import setup, find_packages

setup(
    name='pycos',
    version='0.0.1',
    description='Package for interacting with IBM Cloud Object Store',
    author='John D Sheehan',
    author_email='john.d.sheehan@ie.ibm.com',
    license='Apache 2.0',
    python_requires='>=3.6',
    install_requires=[
        'ibm-cos-sdk==2.5.4'
    ],
    url='https://github.com/IBM/pycos',
    packages=find_packages(where='./src', exclude=['docs', 'tests']),
    include_package_data=True,
    package_dir={"": "src"}
)
