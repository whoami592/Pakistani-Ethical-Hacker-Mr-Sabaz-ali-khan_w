#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# S4B4Z_KH4N_P4K1_CY83R - P4K1ST4N'S CYB3R SH3R
# CHALO, H4CK K4RT3 H4IN! ????

import random
import string
import time

def S4B4Z_P4SSW0RD_G3N3R4T0R(length=16):
    # Y4RR, T1M3 T0 CR34T3 S0M3 KH4OFN4K P4SSW0RDS!
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
    return ''.join(random.choice(chars) for _ in range(length))

def CY83R_D1SPL4Y():
    print("\033[1;32m" + "="*50)
    print("?? S4B4Z_KH4N_P4K1_CY83R H4CK1NG T00L ??")
    print("P4K1ST4N CYB3R F0RC3 - D3KH0 BH4I! ??")
    print("="*50 + "\033[0m")

def M41N_H4CK():
    # H4CK3R M0D3: 0N! L3T'S M4K3 IT QU41D ??
    CY83R_D1SPL4Y()
    print("\n[*] G3N3R4T1NG KH4OFN4K P4SSW0RD...")
    time.sleep(1)  # DR4M4T1C P4US3, Y4RR!
    
    for _ in range(3):
        p4ss = S4B4Z_P4SSW0RD_G3N3R4T0R()
        print(f"\033[1;31m[+] H4CK3D P4SSW0RD: {p4ss}\033[0m")
        time.sleep(0.5)
    
    print("\n\033[1;33m[!] S4B4Z_KH4N S4YS: ST4Y CY83R, ST4Y P4K1! ??\033[0m")

if __name__ == "__main__":
    try:
        M41N_H4CK()
    except KeyboardInterrupt:
        print("\n\033[1;31m[-] H4CK AB0RT3D! CH4L0, N1K4L0! ??\033[0m")