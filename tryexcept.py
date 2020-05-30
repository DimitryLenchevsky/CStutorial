


#try:
#    pass
#except:
#    pass
#else:
#    pass
#finally:
#    pass


def calc(m):
    #1000 : 10 = m : x
    try:
        m = int(m)
    except Exception:
        print('Something went wrong!')
    else:
        return 10 * m / 1000
    finally:
        print('Hi!')

print(calc(1000))