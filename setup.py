from setuptools import setup, find_packages

setup(
    name='snpoiss_bind_n_seq',
    version='0.1.0',
    author='Shreya Sharma, PhD student @IITR',
    Author_email='shreya_s.iitr.ac.in',
    description='A tool for SNP-based Poisson binding analysis on SNP-bind-n-seq sequencing data',
    license='MIT',
    url='https://github.com/Shreya-droid/SNPoiss_bind_n_seq',
    py_modules=['run_all'],
    packages=find_packages(include=['scripts', 'scripts.*']),
    install_requires=['tensorflow'],
    entry_points={
        'console_scripts': [
            'snpoiss_bind_n_seq = snpoiss_bind_n_seq.run_all:main',
        ],
    },
    include_package_data=True,
)
