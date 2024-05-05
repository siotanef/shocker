from setuptools import setup, find_packages

setup(
    name='shocker',
    version='0.1.0',
    description='PySpark extension for relation algebra operators and dataframe keys.',
    author='Fabio Siotane',
    author_email='siotanef@proton.me',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pyspark',
    ],
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Typing :: Typed',
    ],
)