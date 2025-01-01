from setuptools import find_packages, setup
import re

DESCRIPTION = "The spectruM AnAlysis Tools for Python, or MaatPy, is a Python package to analyze scientific data, with a special focus in spectral data from INS, FTIR and Raman, among others."

with open('maatpy/constants.py', 'r') as f:
    content = f.read()
    version_match = re.search(r"version\s*=\s*'([^']+)'", content)
    if not version_match:
        raise RuntimeError("Unable to find version.")
    VERSION = version_match.group(1)

with open('README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='maatpy', 
    version=VERSION,
    author='Pablo Gila-Herranz',
    author_email='pgila001@ikasle.ehu.eus',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=['maatpy'],
    install_requires=['numpy', 'matplotlib', 'pandas', 'scipy'],
    extras_requires={
        'dev': ['pytest', 'twine']
        },
    python_requires='>=3',
    license='AGPL-3.0',
    keywords=['python', 'Maat', 'MaatPy', 'Inelastic Neutron Scattering', 'INS', 'Raman', 'ATR', 'FTIR', 'spectroscopy', 'spectra', 'analysis'],
    classifiers= [
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Other OS",
    ]
)

