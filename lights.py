import requests
import sys
from home_vars import hub_ip, user


on = '{"on":true, "bri":254}'
off = '{"on":false, "transitiontime":50, "bri":254}'


def light_handle(light):
    handle = 'http://' + hub_ip + '/api/' + user + '/lights/' + light + '/state'
    return handle


def light_off(light):
    r = requests.put(light_handle(light), off)
    print('Dim to off.')


def light_on(light):
    r = requests.put(light_handle(light), on)
    print('Light on.')


def dim_level(light,dim):
    bri = 254 * dim / 100
    state = '{"on":true, "bri":' + str(int(bri)) + '}'
    r = requests.put(light_handle(light), state)
    print(state)
    print('Dimmed ' + light + ' to ' + str(dim) + '%')


while True:
    light = input('Select light (1-4) or quit (q): ')
    if light == 'q':
        sys.exit()

    elif 1 <= int(light) <= 4:
        dim = input('Enter dimming level: ')
        dim = int(dim)

        if dim == 0:
            light_off(light)

        elif 0 < dim <= 100:
            dim_level(light,dim)

        else:
            print('Enter a value between 0 and 100.')
