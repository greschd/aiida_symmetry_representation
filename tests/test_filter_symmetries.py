#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, unicode_literals

import pytest
import numpy as np
import pymatgen as mg

@pytest.fixture(params=['POSCAR', 'POSCAR_110_bi_0.04'])
def filter_symmetries_inputs(request, sample, get_process_inputs):
    from aiida.orm import DataFactory

    process, inputs = get_process_inputs(
        calculation_string='symmetry_representation.filter_symmetries',
        code_string='symmetry_repr'
    )

    inputs.symmetries = DataFactory('singlefile')(file=sample('symmetries.hdf5'))

    structure = DataFactory('structure')()
    structure.set_pymatgen_structure(
        mg.Structure.from_file(sample(request.param))
    )
    inputs.structure = structure
    return process, inputs

def test_filter_symmetries(configure_with_daemon, filter_symmetries_inputs):
    from aiida.work.run import run

    process, inputs = filter_symmetries_inputs
    output = run(process, **inputs)

    assert 'symmetries' in output
