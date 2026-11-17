"""Write one relaxing text to the output file.

Deterministic, standard library only, no network. The text is a single
quiet piece of prose, written to slow the reader down.
"""

import os

TEXT = (
    "The kitchen light is still on, low and amber, and outside the window "
    "the street has gone quiet. A cup sits on the table where you left it, "
    "the tea gone cool, the last of its steam faded a while ago. Down the "
    "hall a clock ticks, not hurrying, just keeping its own small time.\n\n"
    "The cat has folded herself into the warmest corner of the couch, paws "
    "tucked in, dreaming whatever cats dream, and the blanket over the "
    "armrest has slipped a little, the way it always does. The fridge hums "
    "its one low note. Beyond the glass, rain begins to tap the leaves, "
    "one drop, then another, then a soft uneven patter that asks for "
    "nothing.\n\n"
    "Nothing in the room is in a hurry. The lamp stays on. The rain keeps "
    "its slow conversation with the roof, one drop at a time, and the cup, "
    "the clock, the sleeping cat and the quiet street all hold their places, "
    "the way things do when nothing is being asked of them."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
