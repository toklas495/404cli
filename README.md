# 404cli 🏴‍☠️

A lean, hacker‑grade CLI tool for writing, managing, and publishing your hack writeups to the **404Nation** platform.

---

## ⚡ Installation

\`\`\`bash
git clone https://github.com/toklas495/404cli.git
cd 404cli
pip install -e .
\`\`\`

Now you can use:

\`\`\`bash
404cmd
\`\`\`

---

## 🧪 Getting Started

### 1. Set Your CLI Token

Grab a \`cli_…\` token from your 404Nation dashboard and save it:

\`\`\`bash
404cmd set --token cli_<YOUR_TOKEN>
\`\`\`

✅ Token is saved at \`~/.config/404cli/config.json\`

---

## ✍️ Commands

### Push Hack

\`\`\`bash
404cmd push hack.md --draft
\`\`\`

### Read Hack

\`\`\`bash
404cmd read
404cmd read --id abc123
\`\`\`

### Update Hack

\`\`\`bash
404cmd update --id abc123 --draft
\`\`\`

### Whoami

\`\`\`bash
404cmd whoami
\`\`\`

### Search

\`\`\`bash
404cmd search "title:jwt && @latest"
\`\`\`

---

## ⚙️ Configuration & Metadata

- \`~/.config/404cli/config.json\` — CLI token
- \`~/.config/404cli/.404meta.json\` — last pushed hack

---

## ✅ CLI Patterns & UX

- Defaults to last pushed ID
- Clean exit codes
- \`--json\` outputs raw data
- Reads open in \`less\`

---

## 🔧 Developer Guide

- Python + \`typer\`, \`rich\`, \`requests\`
- \`utils/\` → parser, editor utils
- \`commands/\` → each CLI command

---

## 🛠 Future Improvements

- Add \`list\` or \`log\` command
- Support \`--slug\` filter
- Autocomplete, usage hints
- \`404cmd render hack.md\`

---

## ⚖️ License

MIT — fork and customize freely.

---

## 🚀 Feedback

Open issues or PRs at:  
[github.com/toklas495/404cli](https://github.com/toklas495/404cli)
