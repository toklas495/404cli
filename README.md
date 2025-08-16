
# 404cli 🏴‍☠️

A lean, hacker-grade CLI tool for writing, managing, and publishing your hack writeups to the **404Nation** platform.

---

## ⚡ Installation

```bash
git clone https://github.com/toklas495/404cli.git
cd 404cli
pip install -e .
```

Now you can run:

```bash
404cmd
```

---

## 🧪 Getting Started

### 1. Set Your CLI Token

Grab a `cli_…` token from your 404Nation dashboard and save it:

```bash
404cmd set --token cli_<YOUR_TOKEN>
```

✅ Token is stored at `~/.config/404cli/config.json`

---

## ✍️ Commands

### Push Hack

```bash
404cmd push hack.md --draft
```

### Read Hack

```bash
404cmd read --id abc123
404cmd read --slug my-first-hack
404cmd read              # defaults to last hack
```

### Update Hack

```bash
404cmd update --id abc123 --draft
404cmd update --slug my-first-hack
```

### Preview Hack (local only)

```bash
404cmd preview hack.md
```

Renders your Markdown in the terminal using `rich` — same as it appears on 404Nation.

### Whoami

```bash
404cmd whoami
```

### Search

```bash
404cmd search "title:jwt && @latest"
```

---

## ⚙️ Configuration & Metadata

* `~/.config/404cli/config.json` → stores your CLI token
* `~/.config/404cli/.404meta.json` → tracks last pushed hack

---

## ✅ CLI Patterns & UX

* Defaults to last pushed ID/slug
* Clean exit codes for scripting
* `--json` outputs raw API response
* `read` + `preview` use `less` for smooth paging

---

## 🔧 Developer Guide

* Built with **Python**, `typer`, `rich`, `requests`
* `utils/` → parsing, editor, meta helpers
* `commands/` → individual CLI commands

---

## 🛠 Roadmap

* `list` / `log` commands
* `--slug` support (✅ added)
* Autocomplete + usage hints
* `404cmd render hack.md` to HTML

---

## ⚖️ License

MIT — fork and hack freely.

---

## 🚀 Feedback

Open issues or PRs at:
[github.com/toklas495/404cli](https://github.com/toklas495/404cli)

---

