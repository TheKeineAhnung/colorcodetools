import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='colortools',
    version='0.0.0',
    author='Keine Ahnung',
    author_email='kontakt@keineahnung.eu',
    description='Some powerfull color tools',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/TheKeineAhnung/colortools',
    project_urls={
        'Bug Tracker': 'https://github.com/TheKeineAhnung/colortools/issues',
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