#Diz ao sistema operacional para usar o Python 3 localizado no ambiente do 
# usuário (via env) para executar o script.:
#!/usr/bin/env python3

"""Hello World Multi Línguas.

Dependendo da língua configurada no ambiente o programa
exibe  amensagem correspondente.

Como usar:
Tenha a varável LANG devidamente configurada ex:
     export LANG=pt_BR

Execução:
python3 hello.py
ou
./hello.py
"""
__version__ = "0.0.1"
__author__ = "Meiriane Ferreira"
__licence__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US") [:5]

msg = "Hello World!"

if current_language == "pt_BR":
    msg = "Óla Mundo!"
elif current_language == "it_IT":
    msg = "Ciao Mondo!"


print(msg)