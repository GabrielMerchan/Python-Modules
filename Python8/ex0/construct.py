#!/usr/bin/env python3

import sys
import os
import site



def global_env() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print(f"\nCurrent Python: {sys.executable}"
          "\nVirtual Environment: None detected")
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("\nTo enter the construct, run:"
          "\npython -m venv env"
          "\nsource env/bin/activate # On Unix"
          "\nenv\\Scripts\\activate # On Windows"
          "\n\nThen run this program again.")


def virtual_env() -> None:
    print("MATRIX STATUS: Welcome to the construct")
    print(f"\nCurrent Python: {sys.executable}"
          f"\nVirtual Environment: {os.path.basename(ruta)}"
          f"\nEnviroment Path: {ruta}")
    print("\nSUCCESS: You're in an isolated environment!"
          "\nSafe to install packages without affecting"
          "\nthe global system.")
    print("\nPackage installation path:"
          f"\n{site.getsitepackages()[0]}")


ruta = os.getenv("VIRTUAL_ENV")

if ruta:
    virtual_env()
else:
    global_env()
