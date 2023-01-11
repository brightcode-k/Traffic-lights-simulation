from trafficSimulator import *


print("""
CONFIG
1: {
    'curve': 2,
    'size': 12
},
2: {
    'curve': 20,
    'size': 100
},
3: {
    'curve': 3,
    'size': 40
},
4: {
    'curve': 200,
    'size': 5
},
5: {
    'curve': 7,
    'size': 40
}
"""
)
inp = int(input('Choose configuration:\n'))


def choose_config(num, conf, key):
    val = conf.get(num).get(key)
    return val


config = {
    1: {
        'curve': 2,
        'size': 12
    },
    2: {
        'curve': 20,
        'size': 100
    },
    3: {
        'curve': 3,
        'size': 40
    },
    4: {
        'curve': 50,
        'size': 90
    },
    5: {
        'curve': 7,
        'size': 40
    }
}
curve = choose_config(inp, config, 'curve')
size = choose_config(inp, config, 'size')
n = 15
length = 300


def main():
    sim = Simulation()

    # Nodes
    WEST_RIGHT_START = (-size - length, curve)
    WEST_LEFT_START = (-size - length, -curve)

    SOUTH_RIGHT_START = (curve, size + length)
    SOUTH_LEFT_START = (-curve, size + length)

    EAST_RIGHT_START = (size + length, -curve)
    EAST_LEFT_START = (size + length, curve)

    NORTH_RIGHT_START = (-curve, -size - length)
    NORTH_LEFT_START = (curve, -size - length)


    WEST_RIGHT = (-size, curve)
    WEST_LEFT =	(-size, -curve)

    SOUTH_RIGHT = (curve, size)
    SOUTH_LEFT = (-curve, size)

    EAST_RIGHT = (size, -curve)
    EAST_LEFT = (size, curve)

    NORTH_RIGHT = (-curve, -size)
    NORTH_LEFT = (curve, -size)

    # Roads
    WEST_INBOUND = (WEST_RIGHT_START, WEST_RIGHT)
    SOUTH_INBOUND = (SOUTH_RIGHT_START, SOUTH_RIGHT)
    EAST_INBOUND = (EAST_RIGHT_START, EAST_RIGHT)
    NORTH_INBOUND = (NORTH_RIGHT_START, NORTH_RIGHT)

    WEST_OUTBOUND = (WEST_LEFT, WEST_LEFT_START)
    SOUTH_OUTBOUND = (SOUTH_LEFT, SOUTH_LEFT_START)
    EAST_OUTBOUND = (EAST_LEFT, EAST_LEFT_START)
    NORTH_OUTBOUND = (NORTH_LEFT, NORTH_LEFT_START)

    WEST_STRAIGHT = (WEST_RIGHT, EAST_LEFT)
    SOUTH_STRAIGHT = (SOUTH_RIGHT, NORTH_LEFT)
    EAST_STRAIGHT = (EAST_RIGHT, WEST_LEFT)
    NORTH_STRAIGHT = (NORTH_RIGHT, SOUTH_LEFT)

    WEST_RIGHT_TURN = turn_road(WEST_RIGHT, SOUTH_LEFT, TURN_RIGHT, n)
    WEST_LEFT_TURN = turn_road(WEST_RIGHT, NORTH_LEFT, TURN_LEFT, n)

    SOUTH_RIGHT_TURN = turn_road(SOUTH_RIGHT, EAST_LEFT, TURN_RIGHT, n)
    SOUTH_LEFT_TURN = turn_road(SOUTH_RIGHT, WEST_LEFT, TURN_LEFT, n)

    EAST_RIGHT_TURN = turn_road(EAST_RIGHT, NORTH_LEFT, TURN_RIGHT, n)
    EAST_LEFT_TURN = turn_road(EAST_RIGHT, SOUTH_LEFT, TURN_LEFT, n)

    NORTH_RIGHT_TURN = turn_road(NORTH_RIGHT, WEST_LEFT, TURN_RIGHT, n)
    NORTH_LEFT_TURN = turn_road(NORTH_RIGHT, EAST_LEFT, TURN_LEFT, n)

    sim.create_roads([
        WEST_INBOUND,
        SOUTH_INBOUND,
        EAST_INBOUND,
        NORTH_INBOUND,

        WEST_OUTBOUND,
        SOUTH_OUTBOUND,
        EAST_OUTBOUND,
        NORTH_OUTBOUND,

        WEST_STRAIGHT,
        SOUTH_STRAIGHT,
        EAST_STRAIGHT,
        NORTH_STRAIGHT,

        *WEST_RIGHT_TURN,
        *WEST_LEFT_TURN,

        *SOUTH_RIGHT_TURN,
        *SOUTH_LEFT_TURN,

        *EAST_RIGHT_TURN,
        *EAST_LEFT_TURN,

        *NORTH_RIGHT_TURN,
        *NORTH_LEFT_TURN
    ])

    def road(a):
        return range(a, a+n)


    sim.create_gen({
        'vehicle_rate': 20,
        'vehicles': [
            [3, {'path': [0, 8, 6]}],
            [1, {'path': [0, *road(12), 5]}],
            [1, {'path': [0, *road(12+n), 7]}],

            [3, {'path': [1, 9, 7]}],
            [1, {'path': [1, *road(12+2*n), 6]}],
            [1, {'path': [1, *road(12+3*n), 4]}],


            [3, {'path': [2, 10, 4]}],
            [1, {'path': [2, *road(12+4*n), 7]}],
            [1, {'path': [2, *road(12+5*n), 5]}],

            [3, {'path': [3, 11, 5]}],
            [1, {'path': [3, *road(12+6*n), 4]}],
            [1, {'path': [3, *road(12+7*n), 6]}]
        ]})

    sim.create_signal([[0, 2], [1, 3]])
    win = Window(sim)
    win.zoom = 5
    win.run(steps_per_update=7)

# Start simulation
main()