from setuptools import setup, find_packages


setup(
    name="monero-checkout",
    version="0.0.1",
    author="Mikaio Faria Damaceno",
    author_email="mikaiodev@gmail.com",
    description="A python tool to handler monero payments",
    url="https://github.com/Mika-IO/monero-checkout",
    project_urls={
        "Bug Tracker": "https://github.com/Mika-IO/monero-checkout/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)
