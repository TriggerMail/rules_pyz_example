import sys

print('sys.path: %s' % repr(sys.path))
import google
print('google: %s' % repr(google))
from google.cloud import bigquery
from google.cloud import storage

def main():
    print('hello world!')
    print('google.cloud.bigquery: %s' % repr(bigquery))
    print('google.cloud.storage: %s' % repr(storage))

if __name__ == '__main__':
    main()
