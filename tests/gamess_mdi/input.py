import qcengine as qcng
import qcelemental as qcel

mol = qcel.models.Molecule.from_data("""
O  0.0  0.000  -0.0683
H  0.0 -0.791  0.543
H  0.0  0.791  0.543
""")

#inp = qcel.models.AtomicInput(
#    molecule=mol,
#    driver="energy",
#    model={"method": "SCF", "basis": "STO"},
#    keywords={"basis__ngauss": "3",
#              "scf__dirscf": ".TRUE.", 
#              "guess__guess": "HUCKEL", 
#              "contrl__units": "BOHR",
#              "contrl__maxit": "60"}
#    )

#ret = qcng.compute(inp, "gamess")

o = qcng.MDIServer(mdi_options = "-role ENGINE -name QM -method TCP -port 8021 -hostname localhost",
                   program = "gamess",
                   molecule = mol,
                   model={"method": "SCF", "basis": "STO"},
                   keywords={"basis__ngauss": "3",
                             "scf__dirscf": ".TRUE.", 
                             "guess__guess": "HUCKEL", 
                             "contrl__units": "BOHR",
                             "contrl__maxit": "60"}
                  )
o.start()


#print("Hello")
#print("ret: ",str(ret))
#print("Energy: " + str(ret.return_result))
##print("ERROR: ", str(ret.error.error_message))
