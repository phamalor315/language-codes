import sys
import time

def progress_bar_loading(duration):
    for i in range(101):
        print(f'Loading: {i}%', end='\r')
        time.sleep(duration / 100)

progress_bar_loading(5)
print('complete')

def progress_bar_loading(duration):
    for i in range(101):
        print(f'Loading: {i}%', end='\r')
        time.sleep(duration / 100)

progress_bar_loading(5)
print('complete')

def progress_bar_loading(duration):
    for i in range(101):
        print(f'Loading: {i}%', end='\r')
        time.sleep(duration / 100)

progress_bar_loading(5)
print('complete')

time.sleep(10)

def loading_bar(duration):
    for i in range(101):
        time.sleep(duration / 100)
        sys.stdout.write(f'\rLoading: {i}%')
        sys.stdout.flush()
    print('\nDone!')

loading_bar(5)

time.sleep(3)

print('Hello, World!')
input('Press the spacebar to continue...')
