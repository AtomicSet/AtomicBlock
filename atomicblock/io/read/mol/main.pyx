from typing import List
import prody


cpdef object mol(str f_topo, traj: List[str]):
    """
    Load a molecule along with its trajectories

    Args:
        f_topo (str): input topology file name
        traj (List[str]): a list of trajectory file names

    Returns:
        AtomGroup: a prody.atomic.atomgroup object
    """
    return prody.parsePDB(f_topo)
