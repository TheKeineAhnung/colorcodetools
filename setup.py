import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='colorcodetools',
    version='0.3.0',
    author='Keine Ahnung',
    author_email='kontakt@keineahnung.eu',
    description='Some powerful color tools',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/TheKeineAhnung/colorcodes',
    project_urls={
        'Bug Tracker': 'https://github.com/TheKeineAhnung/colorcodes/issues',
    },
    license='LICENSE',
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    packages=setuptools.find_packages(),
    python_requires='>=3.6'
)