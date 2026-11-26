import os

ENTRY = "Forgive me for chewing the corner; your cheap paper goes in as a sheet and leaves as confetti."


def output_directory():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    output_dir = output_directory()
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "wb") as output_file:
        output_file.write(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
