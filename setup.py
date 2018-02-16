from setuptools import setup, find_packages

setup(
    name='pydrummer',
    version='0.1',
    description='a minimal drum machine',
    url='http://github.com/allieoop/pydrummer',
    author='Allie Crevier',
    author_email='okay@allie.is',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={
        'samples': ['*.wav'],
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'numpy',
        'sounddevice',
        'soundFile'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
