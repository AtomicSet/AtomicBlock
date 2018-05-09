from . import mol
import atomicblock.data.path as path
def test_mol():
    f_topo = path(os.path.join("pdb", "3j5p.pdb"))
    results   = mol(f_topo, [])
    expected  = prody.pasePDB(f_topo)
    assert results == expected
