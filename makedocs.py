'''
This script is used to update Maat documentation automatically.
Requires pdoc, install it with `pip install pdoc`.
It also requires Thoth, get it here: https://github.com/pablogila/Thoth
Run this script as `python3 makedocs.py`.
'''

import thoth as th

readme = './README.md'
temp_readme = './_README_temp.md'
version_path = './maat/constants.py'

fix_dict ={
    '[alias](https://pablogila.github.io/Maat/maat/alias.html)'             : '`maat.alias`',
    '[classes](https://pablogila.github.io/Maat/maat/classes.html)'         : '`maat.classes`',
    '[constants](https://pablogila.github.io/Maat/maat/constants.html)'     : '`maat.constants`',
    '[fit](https://pablogila.github.io/Maat/maat/fit.html)'                 : '`maat.fit`',
    '[normalize](https://pablogila.github.io/Maat/maat/normalize.html)'     : '`maat.normalize`',
    '[plot](https://pablogila.github.io/Maat/maat/plot.html)'               : '`maat.plot`',
    '[deuteration](https://pablogila.github.io/Maat/maat/deuteration.html)' : '`maat.deuteration`',
    '[sample](https://pablogila.github.io/Maat/maat/sample.html)'           : '`maat.sample`'
} 

version = th.text.find('version=', version_path, 1)[0]
version = th.extract.string(version, 'version', None, True)

print(f'Updating README to {version}...')
th.text.replace_line(f'# Maat {version}', '# Maat v', readme, 1)

print('Updating docs with Pdoc...')
th.file.from_template(readme, temp_readme, None, fix_dict)
th.call.shell(f"pdoc ./maat/ -o ./docs --mermaid --math --footer-text='Maat {version} documentation'")
th.file.remove(temp_readme)
print('Done!')

