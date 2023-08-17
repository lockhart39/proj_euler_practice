# Find the sum of all the primes below two million

import math
import sys

class euler_tl():

    def __init__(self):
        self.test_str = 'Hello'

    def check_for_prime(self, nbr):
        '''
        If a number is prime, the True boolean value is returned. 
        Otherwise, False is returned. 
        '''
        # 1 is not prime
        if nbr == 1:
            return False
        # check from 2 to sqrt(n)
        # if nbr is divisible by a number from 2 to sqrt(nbr) then it is not prime
        for i in range(2, int(math.sqrt(nbr)) + 1):
            if nbr % i == 0:
                return False
        # if none of the above criteria is met, nbr is prime
        return True

    def pull_primes_below(self, up_to_num):
        '''
        Returns a list of prime numbers up to a certain number (exclusive). 
        '''
        # return a list of prime numbers up to a certain number (EXCLUSIVE)
        prime_list = []
        for num in range(1, up_to_num):
            # if a number if prime, append it to the list
            if self.check_for_prime(num) == True:
                prime_list.append(num)
        return prime_list


def main():
    # define object of euler_tl class
    euler_obj = euler_tl()

    # grab all primes below a given number
    try:
        below_num = sys.argv[1]
        # sys.argv passes it as a str
        below_num_int = int(below_num)
        all_primes_below_list = euler_obj.pull_primes_below(below_num_int)
    except Exception as e:
        print(e)
        print('Pass a number as an argument after executing the script.')
        print('Example: python summation_of_primes.py 100')

    # print the sum of the list of primes
    print('The sum of all primes below ' + str(below_num) + ' is: ' + str(sum(all_primes_below_list)))


if __name__ == '__main__':
    main()
