passwords = ['alpha123', 'hello2026', 'pythonrocks']
passphrases = ['first phrase', 'second phrase', 'third phrase']
result = {password: phrase for password, phrase in zip(passwords, passphrases)}
print(result)
