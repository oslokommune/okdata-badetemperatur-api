import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="okdata-badetemperatur-api",
    version="0.0.1",
    author="Origo Dataplattform",
    author_email="dataplattform@oslo.kommune.no",
    description="Lambda functions to collect and expose water temperatures in Oslo.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oslokommune/okdata-badetemperatur-api",
    packages=setuptools.find_packages(),
    install_requires=[],
)
