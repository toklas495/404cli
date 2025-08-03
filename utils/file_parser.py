import os
import re

MIN_CONTENT_LENGTH = 100

class HackFileParseError(Exception):
    """Custom exception for parsing errors in hack file."""
    pass

# 🔒 Used for file-based pushes
def read_markdown_file(file_path):
    if not os.path.exists(file_path):
        raise HackFileParseError(f"❌ File not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines
    

def parse_markdown_file(lines):
    title = None
    tags = []
    content_lines = []
    found_tags = False
    in_content = False

    for line in lines:
        stripped = line.strip()

        # Skip empty lines at the beginning
        if not stripped and not title:
            continue

        if not title and stripped.startswith("# "):
            title = stripped[2:].strip()
            if not title:
                raise HackFileParseError("❌ Title is empty. Format must be: `# My Awesome Hack`")
            continue

        if not found_tags and stripped.lower().startswith("> tags:"):
            tag_line = stripped[7:].strip()
            if not tag_line:
                raise HackFileParseError("❌ Tags cannot be empty. Use: `> tags: xss, bugbounty`")
            tags = [tag.strip() for tag in tag_line.split(",") if tag.strip()]
            if not tags:
                raise HackFileParseError("❌ No valid tags found. Format must be: `> tags: xss, rce`")
            found_tags = True
            continue

        if title and found_tags:
            in_content = True
            content_lines.append(line)

    # Final validations
    if not title:
        raise HackFileParseError("❌ Missing title. First line must start with `# Your Hack Title`")

    if not found_tags:
        raise HackFileParseError("❌ Missing tags. Add a line like `> tags: xss, bugbounty`")

    if not in_content or not content_lines:
        raise HackFileParseError("❌ Content missing. You need to write your hack details after the title and tags.")

    content = "".join(content_lines).strip()

    if len(content) < MIN_CONTENT_LENGTH:
        raise HackFileParseError(f"❌ Content too short ({len(content)} chars). Minimum {MIN_CONTENT_LENGTH} characters required.")

    return {
        "title": title,
        "tags": tags,
        "content": content
    }

# 🧠 Used for edit/update where we get string from `typer.edit()`
def parse_markdown_string(content_str):
    # Match title
    title_match = re.search(r"^# (.+)", content_str, re.MULTILINE)
    if not title_match:
        raise HackFileParseError("❌ Missing title. It must start with `# Your Hack Title`")
    title = title_match.group(1).strip()

    # Match tags
    tags_match = re.search(r"^> *tags:\s*(.+)", content_str, re.IGNORECASE | re.MULTILINE)
    if not tags_match:
        raise HackFileParseError("❌ Missing or malformed tags. Use `> tags: xss, bugbounty`")
    tags_line = tags_match.group(1).strip()
    tags = [t.strip() for t in tags_line.split(",") if t.strip()]
    if not tags:
        raise HackFileParseError("❌ No valid tags found.")

    # Find where content starts (everything after tags)
    content_start = tags_match.end()
    content = content_str[content_start:].strip()

    if len(content) < MIN_CONTENT_LENGTH:
        raise HackFileParseError(f"❌ Content too short ({len(content)} chars). Minimum {MIN_CONTENT_LENGTH} required.")

    return {
        "title": title,
        "tags": tags,
        "content": content
    }
