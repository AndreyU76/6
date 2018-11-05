# Удовиченко

>>> prog = 'Разработка'
>>> print(type(prog))
<class 'str'>
>>> prog = prog.encode('utf-8')
>>> print(prog)
b'\xd0\xa0\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
>>> dec_str_bytes = b'\xd0\xa0\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
>>> dec_str_bytes = dec_str_bytes.decode('utf-8')
>>> print(dec_str_bytes)
Разработка

>>> prog = 'Сокет'
>>> print(type(prog))
<class 'str'>
>>> prog = prog.encode('utf-8')
>>> print(type(prog))
<class 'bytes'>
>>> print(prog)
b'\xd0\xa1\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82'
>>> dec_str_bytes = b'\xd0\xa1\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82'
>>> dec_str_bytes = dec_str_bytes.decode('utf-8')
>>> print(dec_str_bytes)
Сокет
>>>

>>> prog = 'декоратор'
>>> print(type(prog))
<class 'str'>
>>> prog = prog.encode('utf-8')
>>> print(type(prog))
<class 'bytes'>
>>> print(prog)
b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'
>>> dec_str_bytes = b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'
>>> dec_str_bytes = dec_str_bytes.decode('utf-8')
>>> print(dec_str_bytes)
декоратор
>>>

разработка
%u0440%u0430%u0437%u0440%u0430%u0431%u043E%u0442%u043A%u0430
'\u0440'
p
'\u0430'
a
'\u0437'
з
'\u0440'
р
'\u0430'
a
'\u0431'
б
'\u043E'
о
'\u0442'
т
'\u043А'
к
'\u0430'


Сокет

%u0441%u043E%u043A%u0435%u0442

декоратор
%u0441%u043E%u043A%u0435%u0442


 bytes1 = b'classic'
>>> bytes1
b'classic'
>>> type (bytes1)
<class 'bytes'>
>>> bytes1.hex()
'636c6173736963'
>>> bytes2 =b'\x63\x6c\x61\x73\x73\x69\x63'
>>> bytes2
b'classic'

bytes1 = b'function'
>>> bytes1.hex()
'66756e6374696f6e'
>>> bytes2 =b'\x66\x75\x6e\x63\x74\x69\x6f\x6e'
>>> bytes2
b'function'

 bytes1 = b'method'
>>> bytes1.hex()
'6d6574686f64'
>>> bytes2 =b'\x6d\x65\x74\x68\x6f\x64'
>>> bytes2
b'method'

 bytes1 = b'attribute'
>>> bytes1.hex()
'617474726962757465'
>>> bytes2 =b'\x61\x74\x74\x72\x69\x62\x75\x74\x65'
>>> bytes2
b'attribute'

 bytes1 = b'класс'
  File "<stdin>", line 1
SyntaxError: bytes can only contain ASCII literal characters.
 
  bytes1 = b'функция'
  File "<stdin>", line 1
SyntaxError: bytes can only contain ASCII literal characters.
 
 bytes1 = b'type'
>>> bytes1.hex()
'74797065'
>>> bytes2 =b'\x74\x79\x70\x65'
>>>
>>> bytes2
b'type'

 

>>> enc_str = 'standart'
>>> enc_str_bytes = enc_str.encode('utf-8')
>>> print(enc_str_bytes)
b'standart'
>>> b'standart'.decode('utf-8')
'standart'


 enc_str = 'разработка'
>>> enc_str_bytes = enc_str.encode('utf-8')
>>> print(enc_str_bytes)
b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
>>> b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'.decode
<built-in method decode of bytes object at 0x0000022ABF4B8490>
>>> b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'.decode('utf-8')
'разработка'

 enc_str = 'администрирование'
>>> enc_str_bytes = enc_str.encode('utf-8')
>>> print(enc_str_bytes)
b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'
>>> b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'.decode('utf-8')
'администрирование'


>>> with open('textfile_1.txt', 'r', encoding='utf-8') as f:
...     print(f.read())
...
﻿сетевое программирование
сокет
декоратор