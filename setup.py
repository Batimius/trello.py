import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trello.py",
    version="0.0.6.post2",
    author="Batman212369",
    author_email="batman212369.official@gmail.com",
    description="A simple and user-friendly Python to Trello API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Batman212369/trello.py",
    packages=['trello'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests'],
    python_requires='>=3.6',
)