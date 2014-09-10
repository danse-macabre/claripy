from .claripy import Claripy
from .solvers import BranchingSolver
from .solvers import CompositeSolver
from .backends import BackendZ3, BackendVSA, BackendConcrete
from .datalayer import DataLayer

class ClaripyStandalone(Claripy):
    def __init__(self, model_backend=None, solver_backends=None, parallel=None):
        self.parallel = parallel if parallel is not None else False

        if solver_backends is None:
            b_z3 = BackendZ3()
            b_z3.set_claripy_object(self)
            solver_backends = [ b_z3 ]

        if model_backend is None:
            b_concrete = BackendConcrete()
            b_concrete.set_claripy_object(self)
            model_backend = b_concrete

        Claripy.__init__(self, model_backend, solver_backends, parallel=parallel)
        self.dl = DataLayer()

    def solver(self):
        return BranchingSolver(self)

    def composite_solver(self):
        return CompositeSolver(self)
