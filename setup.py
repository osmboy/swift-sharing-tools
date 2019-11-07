import setuptools
from swift_sharing_tools import __name__, __version__, __author__


setuptools.setup(
    name=__name__,
    version=__version__,
    description="Container sharing tools Openstack Swift.",
    author=__author__,
    author_email="sampsa.penna@csc.fi",
    project_urls={
        "Source": "https://github.com/CSCfi/swift-sharing-tools",
    },
    license="MIT",
    install_requires=[
        "aiohttp",
        "python-swiftclient",
        "keystoneauth1",
        "swift_x_account_sharing "
        "@ git+https://github.com/CSCfi/swift-x-account-sharing.git",
        "swift_sharing_request "
        "@ git+https://github.com/CSCfi/swift-sharing-request.git",
        "fire",
    ],
    extras_require={
        "test": ["tox", "pytest", "pytest-cov", "coverage", "flake8",
                 "flake8-docstrings", "asynctest"],
    },
    packages=[__name__],
    platforms="any",
    entry_points={
        "console_scripts": [
            "swift-publish=swift_sharing_tools.publish:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",
        "Intended Audience ::  Information Technology",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",

        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)