from . import mol
import atomicblock.data.path as path
import os
import prody


def test_mol():
    f_topo = path(os.path.join("pdb", "3j5p.pdb"))
    results = mol(f_topo, [])
    expected = prody.parsePDB(f_topo)
    assert results == expected
