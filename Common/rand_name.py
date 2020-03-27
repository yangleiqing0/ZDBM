import random
import string


class RangName:

    def __init__(self):
        pass

    @staticmethod
    def rand_str(rang_num_str):
        ran_str = None
        if '随机' in rang_num_str:
            ran_str = ''.join(random.sample(string.ascii_letters, 1))+''.join(random.sample(string.ascii_letters + string.digits, eval(rang_num_str[2:])-1))

        return ran_str




if __name__ == '__main__':
    RangName().rand_str()
