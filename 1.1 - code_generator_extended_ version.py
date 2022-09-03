def code_input(start_end:str):
    '''testing input data in correct format for postcodes'''
    code_in = input(f'Podaj {start_end} kod pocztowy w formacie "00-000": ').strip()
    if len(code_in) == 6 and code_in[2] == '-':
        try:
            code_in = code_in.replace('-', '')
            code_in = int(code_in)
            if code_in <= 0:
                print('Wprowadzona wartość musi być większa od 0')
                return code_input(start_end)
            return code_in
        except ValueError:
            print('Podana wartość nie jest prawidłowa, poprawny format to "00-000"')
            return code_input(start_end)
    else:
        print('Podana wartość nie jest prawidłowa, poprawny format to "00-000"')
        return code_input(start_end)

def data_input():
    # asking for postcodes data
    code_start = code_input("początkowy")
    code_end = code_input("końcowy")

    # testing if code_start is lower than code_end
    if code_start > code_end:
        print("Wartość początkowa jest mniejsza niż wartość końcowa! Wprowadź dane od nowa.")
        return data_input()
    else:
        ls = [code_start, code_end]
        return ls

def code_gen():
# range for postcodes
    code_start_end = data_input()
    raw_codes = []

    for code in range(code_start_end[0], code_start_end[1]+1):
        raw_codes.append(code)

    # creating list of postcodes and printing output
    # place to rebuild of postcodes in this format
    # 00-001 - 00-009
    # 00-010 - 00-099
    # 00-100 - 00-999
    # etc...
    rdy_codes = []

    for raw_code in raw_codes:
        code_str = str(raw_code)
        rdy_code = code_str[0:2] + '-' + code_str[2:5]
        rdy_codes.append(rdy_code)

    # removing first and last value in list
    rdy_codes = rdy_codes[1:-1]

    for code in rdy_codes:
        print(code)

code_gen()