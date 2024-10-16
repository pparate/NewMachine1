from Practise7_main_test2 import mtest1


def main():
    print('I am main')
    mtest1()

# this will only be executed when this file is run( __name__ will be equal to __main__
# if this is imported in other file and that file is run then __name__ will be this file(module) name
# so below if will not run


if __name__ == '__main__':
    main()
