def check_sign(data,key):
    if '-' in data[key]:
        return 'red'
    else:
        return 'green'
