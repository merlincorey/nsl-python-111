'''Basic Python test harness for the Python 101 Review'''

from collections import Counter
import sys
import traceback

import review


def test_factorial():
    assert 0 != review.factorial(1)
    assert int == type(review.factorial(1))
    assert 6 == review.factorial(3)
    assert 362880 == review.factorial(9)
    assert 80658175170943878571660636856403766975289505440883277824000000000000L == review.factorial(52)
    

def main():
    counts = Counter()
    print 'Searching for tests.'
    for name, test in globals().iteritems():
        if name.startswith('test_') and callable(test):
            print '\tRunning {}... '.format(name),
            try:
                test()
                print 'OK'
                counts['success'] += 1
            except:
                print 'FAIL'
                counts['fail'] += 1
                print '=' * 32
                traceback.print_exc()
                print '=' * 32                
            finally:
                print
    print '{} Tests ran ({} success, {} fail)'.format(counts['fail'] + counts['success'],
                                                      counts['success'],
                                                      counts['fail'])
    return counts['fail']

if '__main__' == __name__:
    sys.exit(main())
