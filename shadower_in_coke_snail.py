import pyautogui
import pydirectinput
import time
import sys


def key_down(key):
    pydirectinput.keyDown(key)
    time.sleep(0.1)
    pydirectinput.keyUp(key)


def start_command_key():
    """ for the string @ """
    pydirectinput.keyDown('shift')
    time.sleep(0.1)
    pydirectinput.keyDown('2')
    time.sleep(0.1)
    pydirectinput.keyUp('shift')
    pydirectinput.keyUp('2')


def sell_equip():
    # check the game keyboard setting
    # change it "To All"
    key_down('1')

    start_command_key()

    for which_key in list('sell'):
        key_down(which_key)

    key_down('enter')
    key_down('esc')
    print('sell equip success')


def rate_command():
    key_down('1')
    key_down('/')
    for which_key in list('rates'):
        key_down(which_key)
    key_down('enter')
    key_down('esc')
    print('/rates command')


def use_skill_buff():
    # my space skill marco including:
    # meso guard, dagger booster, decent speed infusion
    key_down('space')
    # those skill buff take about 3 seconds
    time.sleep(3)
    key_down('g')
    time.sleep(3)


def shadowstep():
    key_down('a')


def boomerang_step():
    key_down('c')


def shadowstep_with_boomerang_step():
    shadowstep()
    boomerang_step()


def turn_to_where(direction):
    """ direction: "left" | "right" """
    key_down(direction)
    # here is because my game client will open the dialogue after left or right press
    # so I press esc to close it.
    key_down('esc')


def main():
    cycle_count = 0

    time.sleep(2)

    while (True):
        print('cycle: ' + str(cycle_count + 1))

        # if the map have equip to sell
        # the number cycle shoud test the map for it
        if cycle_count % 20 == 0:
            sell_equip()

        if cycle_count % 46 == 0:
            use_skill_buff()

        if cycle_count == 0:
            rate_command()

        move_direction = 'right' if cycle_count % 2 == 0 else 'left'
        turn_to_where(move_direction)

        loop_count = 3
        for i in range(1, loop_count + 1):
            print('No: ' + str(i))
            shadowstep_with_boomerang_step()
            time.sleep(0.21)

            is_final = i == loop_count

            if is_final and move_direction == 'right':
                time.sleep(0.3)
                boomerang_step()

            if is_final and move_direction == 'left':
                shadowstep()

        cycle_count += 1


try:
    main()
except KeyboardInterrupt:
    print('stop the script.')
    sys.exit(0)
