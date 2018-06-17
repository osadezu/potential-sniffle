import requests
from home_vars import hub_ip, user


kay = 'http://' + hub_ip + '/api/' + user + '/lights/2/state'
on = '{"on":true, "bri":254}'
off = '{"on":false, "transitiontime":50, "bri":254}'


def light_off():
    r = requests.put(kay, off)


def light_on():
    r = requests.put(kay, on)


def dim_level(bri):
    bri = str(bri)
    state = '{"on":true, "bri":' + bri + '}'
    r = requests.put(kay, state)
    print('Dimmed to ' + bri + '%')


while True:
    light = input('Select light (1-3) or quit (q): ')
    if light 1
    dim = input('Enter dimming level: ')
    dim = int(dim)
    if dim == 0:
        light_off()

    elif 0 < dim <= 100:
        bri = 254 * dim / 100
        dim_level(int(bri))

    else:
        print('Enter a value between 0 and 100.')
