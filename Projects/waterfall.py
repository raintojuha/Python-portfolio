# Waterfall
# Juha Rainto
# 15-08-2021 past midnight

def main():
    # Amount of numbers to print
    numbers = 100

    i = 1
    while i <= numbers:
        txtBuffer = ''
        if (i%7 == 0):
            txtBuffer += 'divisible by 7'
        
        if ('7' in str(i)):
            if (txtBuffer):
                txtBuffer += ' and '
            txtBuffer += 'contains 7'

        else:
            txtBuffer = i

        print (txtBuffer)
        i += 1

    pass


if __name__ == "__main__":
    main()