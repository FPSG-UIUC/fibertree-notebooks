from fibertree.tensor import Tensor
from fibertree.fiber  import Fiber

#
# To do a dot-product we need a "row" for an output.
# So we represent the vectors as 2-D tensors
#

print("--------------------------------------")
print("Dot product on two single row matrices")
print("--------------------------------------")
print("")

a = Tensor(rank_ids=["M","K"], n=1)
b = Tensor(rank_ids=["M","K"], n=2)
z = Tensor(rank_ids=["M"])

a.print("A Tensor")
b.print("B Tensor")
z.print("Z Tensor")

a_m = a.root()
b_m = b.root()
z_m = z.root()

a_m.print("A Tensor - Rank M")
b_m.print("B Tensor - Rank M")
z_m.print("Z Tensor - Rank M")

for m_coord, (z_ref, (a_k, b_k)) in z_m << (a_m & b_m):
    for k_coord, (a_val, b_val) in a_k & b_k:
        print("Processing: [%s -> ( %s, (%s, %s)]"
              % (k_coord, z_ref, a_val, b_val))

        z_ref += a_val * b_val

z.print("\nZ Tensor")

print("")
print("--------------------------------------")
print("")
