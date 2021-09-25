import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='colorinverter',
    version='0.0.11',
    author='Keine Ahnung',
    author_email='kontakt@keineahnung.eu',
    description='A small color inverter',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/TheKeineAhnung/color-inverter',
    project_urls={
        'Bug Tracker': 'https://github.com/TheKeineAhnung/color-inverter/issues',
    },
    license='LICENSE',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    packages=setuptools.find_packages(),
    python_requires='>=3.6'
)