file = open('logs.txt', 'w')
print('hello world!', 'who is your dad?', sep='/', end='\n', file=file, flush=True)
print('Mike 21 Washington, D.C. ηεΎε°ε', sep='/', end='\t', file=file, flush=True)
file.close()