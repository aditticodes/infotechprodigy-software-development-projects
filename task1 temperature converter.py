def convert_celsius(value, output_scale):
    if output_scale == 'F':
        return value * 1.8 + 32
    elif output_scale == 'K':
        return value + 273.15
    else:
        return value

def convert_fahrenheit(value, output_scale):
    if output_scale == 'C':
        return (value - 32) / 1.8
    elif output_scale == 'K':
        return (value + 459.67) * 5 / 9
    else:
        return value

def convert_kelvin(value, output_scale):
    if output_scale == 'C':
        return value - 273.15
    elif output_scale == 'F':
        return value * 9 / 5 - 459.67
    else:
        return value

while True:

    print('Enter the input temperature value:')
    value = float(input())
    print('Enter the input temperature scale (C, F, or K):')
    input_scale = input().upper()
    print('Enter the output temperature scale (C, F, or K):')
    output_scale = input().upper()

  
    if input_scale == 'C':
        result = convert_celsius(value, output_scale)
    elif input_scale == 'F':
        result = convert_fahrenheit(value, output_scale)
    else:
        result = convert_kelvin(value, output_scale)
    print(f'{value} {input_scale} = {result} {output_scale}')

 
    print('Enter q to quit, or any other key to continue:')
    choice = input()
    if choice.lower() == 'q':
        break