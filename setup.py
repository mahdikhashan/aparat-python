import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "aparat-python",
    version = "0.0.2",
    author = "Mahdi Khashan",
    author_email = "mahdikhashan1@gmail.com",
    description = "Access aparat video sharing api",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://pypi.org/project/aparat-python/",
    license='LICENSE.txt',
    project_urls = {
        "Bug Tracker": "https://github.com/mahdikhashan/aparat-python/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages = ['aparat'],
    python_requires = ">=3.6",
    install_requires=[
       "certifi",
       "charset-normalizer",
       "idna",
       "requests",
       "urllib3",
   ],
)
