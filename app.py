import os
print('os imported')
print('glob imported')
print('os imported')
def run_py():
    for i in range(10):
        print('Hiii')
    with open('akshay.txt', 'w') as f:
        f.write('abcd')


if __name__=='__main__':
    run_py()
