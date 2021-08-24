import qcengine as qcng
import qcelemental as qcel
import os

mol = qcel.models.Molecule.from_data("""
O  0.0  0.000  -0.129
H  0.0 -1.494  1.027
H  0.0  1.494  1.027
""")

o = qcng.MDIServer(mdi_options = os.getenv('MDI_OPTIONS'),
                   program = "psi4",
                   molecule = mol,
                   model = {"method": "SCF", "basis": "sto-3g"},
                   keywords = {"scf_type": "df"})
o.start()
