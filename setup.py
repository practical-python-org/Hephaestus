import setuptools

setuptools.setup(
    name="hephaestus",
    description="An installable version of Hephaestus, primarily for testing purposes.",
    package_dir={"": "./"},
    packages=setuptools.find_packages(where="./"),
    package_data={"hephaestus": ["*.toml"]},
    include_package_data=True,
    install_requires=[
        "aiohttp==3.8.4",
        "aiosignal==1.3.1",
        "async-timeout==4.0.2",
        "attrs==22.2.0",
        "charset-normalizer==3.1.0",
        "py-cord==2.4.1",
        "frozenlist==1.3.3",
        "idna==3.4",
        "multidict==6.0.4",
        "toml==0.10.2",
        "yarl==1.8.2",
        "pandas==2.0.0",
    ],
    classifiers=[
        # see https://pypi.org/classifiers/
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    extras_require={
        "dev": ["check-manifest"],
        # 'test': ['coverage'],
    },
)
