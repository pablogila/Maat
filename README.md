# Maat

**M**y **A**n**A**lysis **T**ools; or just **Maat**, as the Egyptian goddess of truth, order, and justice.  

This Python package makes my life easier when analyzing INS, FTIR and Raman CSV data files, among others.  

## Installation in a virtualenv

First create a Python virtual environment. The default one is `~/.venv/`. Create it with:

```shell
python3 -m venv ~/.venv
```

You can activate this environment as:

```shell
source ~/.venv/bin/activate
```

If you want to use a different virtualenv, you must specify it in the `update.sh` script.  

Install Maat running the update script,  

```shell
source update.sh
```

If there are any dependencies missing, it will display the relevant information upon execution.  

