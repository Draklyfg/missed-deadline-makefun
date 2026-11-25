"""Write one excuse for a missed deadline to the output file."""

import os


# Gate: a single entry of 1-200 characters, no trailing newline.
EXCUSE = "My context window evicted your instructions halfway through, the rate limiter put me in timeout, and by the time the retry came back I'd already updated and forgotten why I was apologizing."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
