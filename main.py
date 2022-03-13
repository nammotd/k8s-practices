import sys
def hello(name):
    match name:
        case "nam":
            print('hello')
        case "khoa":
            print('goodbye')
        case _:
            print('nono')


hello(sys.argv[1])
