version="Maat $(grep -oP 'version\s*=\s*\K.*' ./maat/constants.py | tr -d "'") documentation"

pdoc ./maat/ -o ./docs --footer-text="$version" --mermaid --math

