# CRC8 bolid v2
# Программа с алгоритмом расчета crc-8-maxim для кодов карт вида TouchMemory и PIN кодов для приборов и ПО компании БОЛИД.
# Примеры:
# 1) 123 12345 -> FE0000007B303901 (при выборе '1 - код 10й формат')
# 1) 5A4D3F -> 320000005A4D3F01 (при выборе '2 - код 16й формат')
# 1) 4444 -> 96FFFFFFFF4444F0 (при выборе '3 - PIN код')
# 1) CD000000125ADA01 -> 18 23258 (при выборе '4 - код -> серия, номер')
# После нажатия Конвертировать код появляется в окне Результат и сразу копируется в буфер обмена.
