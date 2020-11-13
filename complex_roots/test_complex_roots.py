import numpy as np
import pytest

import complex_roots as cr

def test_poly():
    f = lambda z: (z - 0.5*1j)*(z + 0.5*1j)

    rect = cr.RootFinderRectangle(real_range=[-1,1], imag_range=[0,1])
    res = rect.calculate(f)
    print(res)

    assert np.abs(res - 0.5*1j) < 1.0e-7

def test_cxroots():
    f = lambda z: (np.exp(2*z)*np.cos(z)-1-np.sin(z)+z**5)*(z*(z+2))**2

    rect = cr.RootFinderRectangle(real_range=[-3,3], imag_range=[-3,3],
                                  n_sample=100,
                                  max_zoom_domains=3)
    res = rect.calculate(f, number_roots=7)

    assert len(res) == 7
