from fibertree.tensor import Tensor
from fibertree.fiber import Fiber

print("--------------------------------------")
print("        Elementwise multiply")
print("--------------------------------------")
print("")


a = Tensor(rank_ids=["M"], n=4)
b = Tensor(rank_ids=["M"], n=5)
z = Tensor(rank_ids=["M"])

a.print("A Tensor")
b.print("B Tensor")
z.print("Z Tensor")

a_m = a.root()
b_m = b.root()
z_m = z.root()

a_m.print("A Tensor - M rank")
b_m.print("B Tensor - M rank")
z_m.print("Z Tensor - M rank")

print("Z < A Fiber")

for coord, (z_ref, (a_val, b_val)) in z_m << (a_m & b_m):
    print("Processing: (%s, (%s, (%s, %s)))"
          % (coord, z_ref, a_val, b_val))

    z_ref += a_val * b_val

z.print("\nZ Tensor")

print("")
print("--------------------------------------")
print("")
