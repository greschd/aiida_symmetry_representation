# -*- coding: utf-8 -*-

import re
from setuptools import setup, find_packages

# Get the version number
with open('./aiida_symmetry_representation/__init__.py') as f:
    match_expr = "__version__[^'\"]+(['\"])([^'\"]+)"
    version = re.search(match_expr, f.read()).group(2).strip()

if __name__ == '__main__':
    setup(
        name='aiida-symmetry-representation',
        version=version,
        description='AiiDA Plugin for symmetry representations.',
        author='Dominik Gresch',
        author_email='greschd@gmx.ch',
        license='MIT',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Plugins',
            'Framework :: AiiDA',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2.7',
            'Topic :: Scientific/Engineering :: Physics'
        ],
        keywords='symmetry representation aiida workflow',
        packages=find_packages(exclude=['aiida']),
        include_package_data=True,
        setup_requires=[
            'reentry'
        ],
        reentry_register=True,
        install_requires=[
            'aiida-core',
            'aiida-tools',
            'pymatgen',
        ],
        extras_require={'test': ['aiida-pytest', 'pytest']},
        entry_points={
            'aiida.calculations': [
                'symmetry_representation.filter_symmetries = aiida_symmetry_representation.calculations.filter_symmetries:FilterSymmetriesCalculation',
            ],
            'aiida.parsers': [
                'symmetry_representation.symmetry = aiida_symmetry_representation.parsers.symmetries:SymmetriesParser',
            ],
        },
    )
