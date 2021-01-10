#!/usr/bin/env python3

import sys

class Ip4Translater:
    def dec_to_bin(self, n):
        return bin(n).replace("0b", "") 

    def translate(self, addr):
      octets = ip.split('.')
      int_string = ""

      for o in octets:
        bval = self.dec_to_bin(int(o))
        bval = str(bval).zfill(8)
        print(f"{o} = {bval}")
        int_string += str(bval).zfill(8)
        print(int_string)
      
      int_val = int(int_string, 2)
      print(int_val)

 
if __name__ == "__main__":
  ip = sys.argv[1]
  Ip4Translater().translate(ip)

