def rep_char(c, n):
    print(c * n)
    
def draw_line_string(msg):
    nstr = len(msg)
    rep_char('-',nstr)
    print(f'{msg}')
    rep_char('-', nstr)

name1 = input('Input his/her name: ')
name2 = ('Welcome to Seoul.')
nstr= len(name1) if len(name1) > len(name2) else len(name2)
draw_line_string(f'Hello, {name1},\n{name2}')
