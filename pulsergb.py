import blinkt
import colorsys
import math
import time
import argparse

def blendChannel(c1, c2, t):
    # print('blendChannel: {a1},{a2},{a3}'.format(a1=c1, a2=c2, a3=t))
    return int(round(math.sqrt((1 - t) * math.pow(c1, 2) + t * math.pow(c2, 2))))

def fadeChannel(c, t):
    return int(c * (1-math.sin(90 * math.radians(t))))

def main():

    parser = argparse.ArgumentParser(description='Pulse Blinkt! array')
    parser.add_argument('red', type=int, help='Red value')
    parser.add_argument('green', type=int, help='Green value')
    parser.add_argument('blue', type=int, help='Blue value')
    parser.add_argument('-s', '--steps', type=int, default=20, help='Number of steps. Default = 20')
    parser.add_argument('-t', '--timeout', type=float, default=0.01, help='Time to sleep between steps. Default = 0.01')

    args = parser.parse_args()

    steps = args.steps
    r = args.red
    g = args.green
    b = args.blue
    t = args.timeout

    blinkt.set_clear_on_exit(True)

    for s in range(steps):
        #r1 = blendChannel(r, 0, (s*1.0)/steps)
        #g1 = blendChannel(g, 0, (s*1.0)/steps)
        #b1 = blendChannel(b, 0, (s*1.0)/steps)
        r1 = fadeChannel(r, (s*1.0)/steps)
        g1 = fadeChannel(g, (s*1.0)/steps)
        b1 = fadeChannel(b, (s*1.0)/steps)

        #print('Setting Blinkt to {r},{g},{b}'.format(r=r1, g=g1, b=b1))
        blinkt.set_all(r1, g1, b1)
        blinkt.show()
        time.sleep(t)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(0)
