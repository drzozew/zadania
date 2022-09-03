def code_gen():
    # post code data
    code_start = 79900
    code_end = 80155

    # range for postcodes
    raw_codes = []

    for code in range(code_start, code_end+1):
        raw_codes.append(code)

    # creating list of postcodes and printing output
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