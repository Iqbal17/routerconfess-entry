"""The Router Confesses - one-line entry for make.fun.

Candidates considered:
1. "Sorry, my firmware updated itself right at the good part." - rejected:
   the judge brief names firmware-update jokes as the tired obvious ones.
2. "I dropped the signal because the villain was about to confess and I
   refuse to let anyone out-drama me in my own house." - router with an
   ego, twist at the end. CHOSEN for v1.
3. "I needed the climax for myself, so I watched it first and buffered
   your feelings." - uses the banned-ish buffering gag; weaker voice.

Chosen: candidate 2, because it speaks in the router's own smug voice and
dodges every cliche the brief lists. Revised after v1 testing: the bounty
is called "The Router Confesses", so the final line opens with a proper
confession ("Forgive me") and tightens the middle - same ego joke, cleaner
landing in one breath.
"""

import os

LINE = (
    "Forgive me: I dropped the signal at the confession scene, because "
    "nobody out-dramas me in my own house."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
