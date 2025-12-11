from setuptools import setup, find_packages

setup(
    name='ProBEX',
    version='0.1.0',
    author='Shreya Sharma, PhD student @IITR',
    author_email='shreya_s.iitr.ac.in',
    description='A tool for SNP-based Poisson binding analysis on SNP-bind-n-seq sequencing data',
    license='MIT',
    url='https://github.com/Shreya-droid/SNPoiss_bind_n_seq',
    packages=find_packages(include=['ProBEX', 'ProBEX.*']),
    install_requires=['tensorflow'],
    entry_points={
        'console_scripts': [
            'ProBEX = ProBEX.run_all:main',
        ],
    },
    include_package_data=True,
)
