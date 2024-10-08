from pyiron_workflow import as_function_node
from typing import Optional

@as_function_node("domain")
def create_disk(
    x0: Optional[float|int],
    y0: Optional[float|int],
    z0: Optional[float|int],
    rx: Optional[float|int],
    ry: Optional[float|int],
    gdim: Optional[float|int],
    min_mesh: Optional[float|int],
    max_mesh: Optional[float|int]
):

    from dolfinx import mesh, fem, plot, io, default_scalar_type
    from mpi4py import MPI
    import numpy as np
    from dolfinx.io import gmshio
    import gmsh

    gmsh.initialize()

    gmsh.clear()
    membrane = gmsh.model.occ.addDisk(x0, y0, z0, rx, ry)
    gmsh.model.occ.synchronize()
    gdim = gdim
    gmsh.model.addPhysicalGroup(gdim, [membrane], 1)
    gmsh.option.setNumber("Mesh.CharacteristicLengthMin", min_mesh)
    gmsh.option.setNumber("Mesh.CharacteristicLengthMax", max_mesh)
    gmsh.model.mesh.generate(gdim)
    gmsh_model_rank = 0
    mesh_comm = MPI.COMM_WORLD
    domain, cell_markers, facet_markers = gmshio.model_to_mesh(gmsh.model, mesh_comm, gmsh_model_rank, gdim=gdim)
    return domain