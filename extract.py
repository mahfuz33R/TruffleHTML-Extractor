import re
import os

def extract_blocks(text):
    """
    Extract: repo URL + its block until next URL.
    """
    pattern = r"(https://github\.com/[^\s]+)([\s\S]*?)(?=https://github\.com/|$)"
    return re.findall(pattern, text)


def clean_html(text):
    """
    Remove HTML tags such as </h3>, <br>, etc.
    """
    return re.sub(r"<[^>]*>", "", text)


def parse_block(block):
    """
    Extract detector type and raw result.
    """
    block = clean_html(block)

    detector = re.search(r"Detector Type:\s*(.+)", block)
    raw = re.search(r"Raw result:\s*(.+)", block)

    if detector and raw:
        return detector.group(1).strip(), raw.group(1).strip()

    return None, None


def choose_output_filename(base_name):
    """
    If file exists, create name1.txt, name2.txt...
    """
    filename = f"{base_name}.txt"
    if not os.path.exists(filename):
        return filename

    i = 1
    while True:
        filename = f"{base_name}{i}.txt"
        if not os.path.exists(filename):
            return filename
        i += 1


def main():
    html_path = input("Enter input HTML file path: ").strip()

    with open(html_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = clean_html(text)
    blocks = extract_blocks(text)

    # ---------------------------------------
    # COLLECT ALL DETECTOR TYPES FIRST
    # ---------------------------------------
    detector_set = set()

    for _, block in blocks:
        detector_type, raw = parse_block(block)
        if detector_type:
            detector_set.add(detector_type)

    # Show available detector types
    print("\nDetected Detector Types:")
    for dt in sorted(detector_set):
        print(" -", dt)

    print("\nPress ENTER to extract ALL detector types")
    desired_detector = input("Enter Detector Type to filter: ").strip()

    match_all = (desired_detector == "")

    # Determine output filename
    if match_all:
        output_file = choose_output_filename("output")
    else:
        output_file = choose_output_filename(desired_detector)

    # ---------------------------------------
    # PROCESS THE BLOCKS
    # ---------------------------------------
    unique_results = {}

    for repo_url, block in blocks:
        detector_type, raw = parse_block(block)

        if raw is None:
            continue

        # filter
        if not match_all and detector_type != desired_detector:
            continue

        if raw not in unique_results:
            unique_results[raw] = {
                "detector": detector_type,
                "repos": set()
            }

        unique_results[raw]["repos"].add(repo_url)

    # ---------------------------------------
    # WRITE OUTPUT
    # ---------------------------------------
    with open(output_file, "w", encoding="utf-8") as f:
        for raw, data in unique_results.items():
            f.write("Detector Type: " + data["detector"] + "\n")
            f.write("Raw result: " + raw + "\n")
            f.write("Repositories:\n")
            for repo in data["repos"]:
                f.write("  - " + repo + "\n")
            f.write("\n" + "-" * 60 + "\n\n")

    print("\n✔ Scan & extraction complete!")
    print(f"✔ Total unique raw results: {len(unique_results)}")
    print(f"✔ Saved to: {output_file}")


if __name__ == "__main__":
    main()
