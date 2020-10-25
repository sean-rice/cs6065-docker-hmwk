# sean rice
# 20201025
# cs6065: docker homework

import pathlib
import socket
from typing import Dict

INPUT_DIR_PATH: pathlib.Path = pathlib.Path("/home/data")
OUTPUT_FILE_PATH: pathlib.Path = pathlib.Path("/home/output/result.txt")

def get_ip() -> str:
    # https://stackoverflow.com/a/28950776
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(("10.255.255.255", 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def word_count(path: pathlib.Path) -> int:
    with path.open("r") as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        words = line.replace(",", "").replace(".", "").replace("  ", " ").split()
        total += len(words)
    return total

def build_output(total_words: int, longest_file: pathlib.Path, ip: str) -> str:
    output = f"total number of words: {total_words}\n"
    output += f"file with most words: {longest_file.name}\n"
    output += f"ip address: {ip}"
    return output

def main():
    path_to_wordcount: Dict[pathlib.Path, int] = {}
    text_files = INPUT_DIR_PATH.glob("*.txt")
    for path in text_files:
        path_to_wordcount[path] = word_count(path)
    
    total_words = sum(path_to_wordcount.values())
    longest_textfile: pathlib.Path = max(path_to_wordcount.keys(), key=lambda k: path_to_wordcount[k])

    ip = get_ip()

    output = build_output(total_words, longest_textfile, ip)

    OUTPUT_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_FILE_PATH.open("w") as outf:
        outf.write(output)
    
    print(output)

if __name__ == "__main__":
    main()
