import setuptools

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="country_catalogue",
    version="0.0.2",
    author="Christopher Okoro",
    author_email="christopherokoro007@gmail.com",
    description="Little information you need Every country",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/uraniumkid30/country_catalogue",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pandas', 'numpy'],
    python_requires='>=3.6',
)
