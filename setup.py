import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wgan-exp-draconus21",
    version="0.0.0",
    author="Neeth Kunnath",
    author_email="neeth.xavier@gmail.com",
    description="Experimenting with WGANs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/draconus21/wgan",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
