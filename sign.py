def check_sign(data):
    if '+' in data['percent']:
        return 'green'
    else:
        return 'red'