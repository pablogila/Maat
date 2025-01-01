'''
This script is used to update Maat documentation automatically.
Requires pdoc, install it with `pip install pdoc`.
It also requires Thoth, get it here: https://github.com/pablogila/ThothPy
Run this script as `python3 makedocs.py`.
'''

try:
    import thotpy as th
except:
    print("Aborting... You need ThotPy to compile the documentation! https://github.com/pablogila/ThotPy")

readme = './README.md'
temp_readme = './_README_temp.md'
version_path = './maatpy/constants.py'

fix_dict ={
    '[alias](https://pablogila.github.io/MaatPy/maatpy/alias.html)'             : '`maatpy.alias`',
    '[classes](https://pablogila.github.io/MaatPy/maatpy/classes.html)'         : '`maatpy.classes`',
    '[constants](https://pablogila.github.io/MaatPy/maatpy/constants.html)'     : '`maatpy.constants`',
    '[atoms](https://pablogila.github.io/MaatPy/maatpy/atoms.html)'             : '`maatpy.atoms`',
    '[elements](https://pablogila.github.io/MaatPy/maatpy/elements.html)'       : '`maatpy.elements`',
    '[fit](https://pablogila.github.io/MaatPy/maatpy/fit.html)'                 : '`maatpy.fit`',
    '[normalize](https://pablogila.github.io/MaatPy/maatpy/normalize.html)'     : '`maatpy.normalize`',
    '[plot](https://pablogila.github.io/MaatPy/maatpy/plot.html)'               : '`maatpy.plot`',
    '[deuteration](https://pablogila.github.io/MaatPy/maatpy/deuteration.html)' : '`maatpy.deuteration`',
    '[sample](https://pablogila.github.io/MaatPy/maatpy/sample.html)'           : '`maatpy.sample`',
}

version = th.find.lines(r"version\s*=", version_path, -1, 0, False, True)[0]
version = th.extract.string(version, 'version', None, True)

print(f'Updating README to {version}...')
th.text.replace_line(f'# MaatPy {version}', '# MaatPy v', readme, 1)

print('Updating docs with Pdoc...')
th.file.from_template(readme, temp_readme, None, fix_dict)
th.call.bash(f"pdoc ./maatpy/ -o ./docs --mermaid --math --footer-text='MaatPy {version} documentation'")
th.file.remove(temp_readme)
print('Done!')

