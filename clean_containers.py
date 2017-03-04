import subprocess

proc = subprocess.Popen(['docker', 'ps', '-a'], stdout=subprocess.PIPE)
counter = 0
while True:
    line = proc.stdout.readline()
    if line != '':
        cols = line.split()
        # Skip header line
        if cols[0] == 'CONTAINER':
            continue
        subprocess.call(['docker', 'rm', cols[0]])
        counter += 1
    else:
        break

print('DONE: %d container%s deleted.' % (counter, 's' if counter > 1 else ''))
