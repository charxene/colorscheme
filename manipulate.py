from hsluv import hex_to_hsluv, hsluv_to_hex
import sys

dh, ds, dl = map(float, sys.argv[1:4])
for h, s, l in map(lambda x: hex_to_hsluv(x.replace("0x", "#")), sys.argv[4:]):
    out = hsluv_to_hex([h+dh, s+ds, l+dl])
    print(out)
