
import crcmod.predefined


def convert_base(num, to_base=10, from_base=10):
    ''' Конвертация числа из одной системы счисления в другую.
    '''
    # Сначала конвертируем в 10й систему.
    n = int(num, from_base) if isinstance(num, str) else num
    # Далее уже конвертируем в 'to_base' систему.
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        n, m = divmod(n, to_base)
        res += alphabet[m]
    return res[::-1]


def calculation_crc(x):
    ''' Расчет CRC8 maxim_dallas. 
        На вход подает число в 10м формате.
    '''
    crc = crcmod.predefined.mkPredefinedCrcFun('crc-8-maxim')(x.to_bytes(7, 'little'))
    crc = convert_base(crc, 16, 10)
    return crc


def code_generation(type_code, code_temp):
    ''' В зависимости от выбранного пользователем типа
        преобразования, код будет подготавливаться к 
        расчету CRC8 maxim_dallas.
    '''
    code_end = ''

    if type_code == '1 - код 10й формат':
        code_start = code_temp.split()
        code_temp1 = convert_base(code_start[0], 16, 10)
        code_temp2 = convert_base(code_start[1], 16, 10)
        code_start = ('0'*(2 - len(code_temp1)) + code_temp1 + 
                      '0'*(4 - len(code_temp2)) + code_temp2)
        code_end = '0'*6 + code_start + '01'
    elif type_code == '2 - код 16й формат':
        code_end = '0'*(12 - len(code_temp)) + code_temp + '01'
    elif type_code == '3 - PIN код':
        code_end = 'F'*(12 - len(code_temp)) + code_temp + 'F0'
    elif type_code == '4 - код -> серия, номер':
        code_temp1 = convert_base(code_temp[8:10], 10, 16)
        code_temp2 = convert_base(code_temp[10:14], 10, 16)
        code_end =  code_temp1 + ',' + code_temp2
        return code_end

    x = int(code_end, 16)
    crc = calculation_crc(x)
    code_end = '0'*(2 - len(crc)) + crc + code_end
    return code_end











