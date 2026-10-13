
import sys

def simInt(p, r, t):
    return (p * r * t) / 100

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python simpleint.py principal rate time")
        sys.exit(1)

    p = float(sys.argv[1])
    r = float(sys.argv[2])
    t = float(sys.argv[3])

    print("simple interest:", simInt(p, r, t))
