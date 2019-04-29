from setuptools import setup

setup(
    name="rfapi",
    version="0.1.3",
    description="Async RedForester API module for Python 3.7+",
    url="https://github.com/ichega/rfapi/",
    author="Pavel Katskov",
    author_email="pasha_kackov@mail.ru",
    license="MIT",
    packages=[
        "rfapi"
    ],
    install_requires=[
        "aiohttp",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha"
    ]
)

