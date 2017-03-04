import subprocess

proc = subprocess.Popen(['docker', 'images'], stdout=subprocess.PIPE)
counter = 0
while True:
    line = proc.stdout.readline()
    if line != '':
        cols = line.split()
        if cols[0] == 'REPOSITORY':
            continue
        if cols[0] == '<none>' and cols[1] == '<none>':
            subprocess.call(['docker', 'rmi', cols[2]])
            counter += 1
    else:
        break

print('DONE: %d container%s deleted.' % (counter, 's' if counter > 1 else ''))
