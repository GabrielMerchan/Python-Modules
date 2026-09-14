#!/usr/bin/env python3

import importlib
def check_mods() -> dict[str, object]:
    mods = {}
    packages = ["pandas", "numpy", "matplotlib", "requests"]
    for package in packages:
        try:
            mod = importlib.import_module(package)
            print(f"[OK] {mod.__name__} ({mod.__version__})")
            mods[package] = mod
        except ModuleNotFoundError as e:
            print(f"{e}. Para instalar usa "
                  f"'pip install {package}'")
    if "matplotlib" in mods:
        mods["matplotlib.pyplot"]= importlib.import_module("matplotlib.pyplot")
    return mods


def data_creation(mods: dict[str, object]) -> list[int]:
    data = mods["numpy"].random.randint(0, 100, 1000)
    return data


def data_manipulation(data: list[int], mods: dict[str, object]) -> None:
    odd_list = []
    even_list = []
    for num in data:
        if (num % 2 == 0):
            even_list.append(num)
        else:
            odd_list.append(num)
    max_len = max(len(odd_list), len(even_list))
    while(max_len > len(odd_list)):
        odd_list.append(None)
    while(max_len > len(even_list)):
        even_list.append(None)
    df = mods["pandas"].DataFrame({"Pares": even_list, "Impares": odd_list})
    data_visualization(df, mods)


def data_visualization(df, mods: dict[str, object]) -> None:
    plt = mods["matplotlib.pyplot"]
    plt.bar(["Even", "Odd"], [df["Pares"].count(), df["Impares"].count()])
    filename = "matrix_analysis.png"
    plt.savefig(filename)
    print("\nAnalysis complete!"
          f"\nResults saved to: {filename}")

if __name__ == "__main__":
    mods = check_mods()
    print("\nAnalyzing Matrix data...")
    numbs = data_creation(mods)
    print(f"Processing {len(numbs)} data points..."
          "\nGenerating visualization...")
    data_manipulation(numbs, mods)



    
