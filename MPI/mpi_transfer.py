from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

filename = "test.txt"
output = "received.txt"

if rank == 0:
    # Sender
    with open(filename, "rb") as f:
        data = f.read()

    comm.send(len(data), dest=1, tag=0)
    comm.Send([data, MPI.BYTE], dest=1, tag=1)

    print("Rank 0: file sent.")

elif rank == 1:
    # Receiver
    size = comm.recv(source=0, tag=0)
    buffer = bytearray(size)

    comm.Recv([buffer, MPI.BYTE], source=0, tag=1)

    with open(output, "wb") as f:
        f.write(buffer)

    print("Rank 1: file received.")

