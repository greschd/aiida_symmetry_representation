#!/usr/bin/env python
# -*- coding: utf-8 -*-

# © 2017-2019, ETH Zurich, Institut für Theoretische Physik
# Author: Dominik Gresch <greschd@gmx.ch>

from __future__ import division, unicode_literals

import pytest
import pymatgen as mg


@pytest.fixture(params=['POSCAR', 'POSCAR_110_bi_0.04'])
def filter_symmetries_inputs(request, sample, get_process_builder):
    from aiida.plugins import DataFactory

    builder = get_process_builder(
        calculation_string='symmetry_representation.filter_symmetries',
        code_string='symmetry_repr'
    )

    builder.symmetries = DataFactory('singlefile')(
        file=sample('symmetries.hdf5')
    )

    structure = DataFactory('structure')()
    structure.set_pymatgen_structure(
        mg.Structure.from_file(sample(request.param))
    )
    builder.structure = structure
    return builder


def test_filter_symmetries(configure_with_daemon, filter_symmetries_inputs):  # pylint: disable=unused-argument
    from aiida.engine import run

    builder = filter_symmetries_inputs
    output = run(builder)

    assert 'symmetries' in output
