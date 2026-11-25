"""make.fun entry: Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one short nostalgic sentence to entry.txt. Python 3.13, stdlib only,
no network, no file reads beyond this source.
"""

import os

TEXT = (
    "At grandmother's house the rice cooker clicked and the kitchen smelled "
    "of rain on hot concrete, and I sat at the low table swinging my legs, "
    "certain that summer evenings like that one would last forever, not "
    "knowing the smell of fresh rice would one day be the fastest way home."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
