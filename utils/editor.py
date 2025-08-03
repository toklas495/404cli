import os
import tempfile
import subprocess

def open_in_editor(initial_content: str) -> str:
    editor = os.environ.get("EDITOR", "nano")

    with tempfile.NamedTemporaryFile(suffix=".md", delete=False) as tmp:
        tmp.write(initial_content.encode())
        tmp.flush()

        subprocess.call([editor, tmp.name])

        # Read the edited content
        with open(tmp.name, "r") as f:
            updated = f.read()

    os.unlink(tmp.name)
    return updated
