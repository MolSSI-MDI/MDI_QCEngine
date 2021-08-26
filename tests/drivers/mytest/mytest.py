import mdi

# Attempt to import mpi4py
try:
    from mpi4py import MPI
    use_mpi4py = True
except ImportError:
    use_mpi4py = False
 
# MPI intra-communicator for all processes running this code
# It should be set to MPI.COMM_WORLD prior to the call to MDI_Init(), as shown below
# Afterwards, you should ALWAYS use this variable instead of MPI.COMM_WORLD
if use_mpi4py:
    world_comm = MPI.COMM_WORLD
else:
    world_comm = None

# Get the command-line options for MDI

# Iniitalize MDI
mdi_options = "-role DRIVER -name driver -method TCP -port 8021"
mdi.MDI_Init(mdi_options)

# Set world_comm to the correct intra-code MPI communicator
world_comm = mdi.MDI_MPI_get_world_comm()

# Get the MPI rank of this process
if world_comm is not None:
    my_rank = world_comm.Get_rank()
else:
    my_rank = 0
 
# Accept a connection from an external driver
mdi_comm = mdi.MDI_Accept_Communicator()

# This is the part where you can use MDI
if my_rank == 0:
    # <NAME
    mdi.MDI_Send_Command("<NAME", mdi_comm)
    engine_name = mdi.MDI_Recv(mdi.MDI_NAME_LENGTH, mdi.MDI_CHAR, mdi_comm)
    print("ENGINE NAME: " + str(engine_name))

    # <ENERGY
    #mdi.MDI_Send_Command("<ENERGY", mdi_comm)
    #energy = mdi.MDI_Recv(1, mdi.MDI_DOUBLE, mdi_comm)
    #print("ENERGY:  " + str(energy))

    # <NATOMS
    mdi.MDI_Send_Command("<NATOMS", mdi_comm)
    natoms = mdi.MDI_Recv(1, mdi.MDI_INT, mdi_comm)
    print("NATOMS: " + str(natoms))

    # <COORDS
    mdi.MDI_Send_Command("<COORDS", mdi_comm)
    coords = mdi.MDI_Recv(3 * natoms, mdi.MDI_DOUBLE, mdi_comm)
    print("COORDS: " + str(coords))

    # >COORDS
    coords[0] += 0.1
    mdi.MDI_Send_Command(">COORDS", mdi_comm)
    mdi.MDI_Send(coords, 3 * natoms, mdi.MDI_DOUBLE, mdi_comm)
    mdi.MDI_Send_Command("<ENERGY", mdi_comm)
    energy = mdi.MDI_Recv(1, mdi.MDI_DOUBLE, mdi_comm)
    print("ENERGY:  " + str(energy))

    # <ELEMENTS
    mdi.MDI_Send_Command("<ELEMENTS", mdi_comm)
    elements = mdi.MDI_Recv(natoms, mdi.MDI_INT, mdi_comm)
    print("ELEMENTS: " + str(elements))

    # <FORCES
    #mdi.MDI_Send_Command("<FORCES", mdi_comm)
    #forces = mdi.MDI_Recv(3 * natoms, mdi.MDI_DOUBLE, mdi_comm)
    #print("FORCES: " + str(forces))

    # EXIT
    mdi.MDI_Send_Command("EXIT", mdi_comm)
