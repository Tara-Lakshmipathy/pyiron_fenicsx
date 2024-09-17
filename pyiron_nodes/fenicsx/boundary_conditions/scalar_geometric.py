from pyiron_workflow import as_function_node
from typing import Optional
from typing import Callable

@as_function_node("bc")
def one_d_scalar_dirichlet(
    function_space,
    bc_function: str,
    value: Optional[float|int]
):
    import numpy as np
    from dolfinx import mesh, fem, plot, io, default_scalar_type

    lazy_evaluation = lambda: eval("bc_function")
    result = lazy_evaluation
    boundary_dofs = fem.locate_dofs_geometrical(function_space, result())
    bc = fem.dirichletbc(default_scalar_type(value), boundary_dofs, function_space)
    return bc

def bc_function(x):
    import numpy as np
    return np.isclose(np.sqrt(x[0]**2 + x[1]**2), 1)
    
@as_function_node("bc")
def circular_unit_func_dirichlet(
    function_space,
    #bc_function: Callable,
    value: Optional[float|int]
):
    import numpy as np
    from dolfinx import mesh, fem, plot, io, default_scalar_type
    
    boundary_dofs = fem.locate_dofs_geometrical(function_space, globals()['bc_function'])
    bc = fem.dirichletbc(default_scalar_type(value), boundary_dofs, function_space)
    return bc