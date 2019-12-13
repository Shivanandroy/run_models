import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    #Here is the module name.
    name="run_models",

    #version of the module
    version="0.0.2",

    #Name of Author
    author="Shivanand Roy",

    #your Email address
    author_email="Shivanandroy.official@gmail.com",

    #Small Description about module
    description="Run all regression and classification models with its default parameters",

    long_description=long_description,

    #Specifying that we are using markdown file for description
    long_description_content_type="text/markdown",

    #Any link to reach this module, if you have any webpage or github profile
    url="https://github.com/Shivanandroy/run_models/",
    packages=setuptools.find_packages(),

    #classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['scikit-learn','warnings','xgboost','lightgbm','catboost','pandas','matplotlib','numpy']
)
