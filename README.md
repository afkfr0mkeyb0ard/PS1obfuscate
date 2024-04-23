# PS1obfuscate
Obfuscate Powershell scripts

---> Takes a PS1 script and writes a new obfuscated one (myscript.ps1 --> **myscript-OBFUSCATED.ps1**)

### Remove empty lines
```> python3 PS1obfuscate.py myfile.ps1 -E```

### Remove comments
```> python3 PS1obfuscate.py myfile.ps1 -C```

### Rename functions
```> python3 PS1obfuscate.py myfile.ps1 -F```

### Rename variables
```> python3 PS1obfuscate.py myfile.ps1 -V```

### Do all
```> python3 PS1obfuscate.py myfile.ps1```

### Example with Winpeas

![ctf](https://github.com/afkfr0mkeyb0ard/PS1obfuscate/assets/123593001/2b8ba424-0fb2-471c-a835-a8603878a4b0)
