from typing import List
from prody.atomic.atomgroup import AtomGroup
"""
Load a molecule along with its trajectories
"""
cpdef mol(f_topo: str, traj: List[str]) -> AtomGroup:
    return prody.parsePDB(f_topo)
