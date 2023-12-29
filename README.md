# PS1obfuscate
Obfuscate Powershell scripts

---> Takes a PS1 script and writes a new obfuscated one (myscript.ps1 --> **myscript.ps1_OBF**)

#### Remove comments
> python3 PS1obfuscate.py myfile.ps1 -C

#### Rename functions
> python3 PS1obfuscate.py myfile.ps1 -F

#### Rename variables
> python3 PS1obfuscate.py myfile.ps1 -V

#### Do all
> python3 PS1obfuscate.py myfile.ps1
