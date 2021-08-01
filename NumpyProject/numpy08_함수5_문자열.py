import numpy as np

'''
  np.char.문자열함수
    
'''
print(dir(np.char))
'''
'add', 'array', 'array_function_dispatch', 'asarray', 'asbytes', 'bool_', 
'capitalize', 'center', 'character', 'chararray', 'compare_chararrays', 
'count', 'decode', 'encode', 'endswith', 'equal', 'expandtabs', 'find', 
'functools', 'greater', 'greater_equal', 'index', 'int_', 'integer', 'isalnum', 
'isalpha', 'isdecimal', 'isdigit', 'islower', 'isnumeric', 'isspace', 'istitle', 
'isupper', 'join', 'less', 'less_equal', 'ljust', 'lower', 'lstrip', 'mod', 
'multiply', 'narray', 'ndarray', 'not_equal', 'numpy', 'object_', 'overrides', 
'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 
'set_module', 'split', 'splitlines', 'startswith', 'str_len', 'string_', 'strip', 
'swapcase', 'sys', 'title', 'translate', 'unicode_', 'upper', 'zfill']

'''
# 1. 첫글자 대문자
arr = np.array(["hElLo SOmEThinG","HaPPy anYthiNG","wOrlD NoThIng"])
# 일반적인 방법
# list = []
# for s in arr:
#     print(s.capitalize())
#     list.append(s.capitalize())
# print(np.array(list))

print("1. 첫글자 대문자:", np.char.capitalize(arr))  # ['Hello' 'Happy' 'World']
print("2. 대문자:", np.char.upper(arr))  # ['HELLO' 'HAPPY' 'WORLD']
print("3. 소문자:", np.char.lower(arr))  # ['hello' 'happy' 'world']
print("4. swapcase:", np.char.swapcase(arr))  # ['HeLlO' 'hAppY' 'WoRLd']
print("4. title:", np.char.title(arr))  # ['Hello Something' 'Happy Anything' 'World Nothing']

####################################################################
arr = np.array(["hello", "world"])
arr2 = np.array(["길동", "이순신"])
print("6. add:", np.char.add(arr, arr2))  # ['hello길동' 'world이순신']
print("7. multiply:", np.char.multiply(arr,2))  # ['hellohello' 'worldworld']

#####################################################################
arr = np.array(["hello", "world"])

print("8. center:", np.char.center(arr, 20, "*")) # ['*******hello********' '*******world********']
print("9. rjust:", np.char.rjust(arr, 20, "*")) # ['***************hello' '***************world']
print("10. ljust:", np.char.ljust(arr, 20, "*")) # ['hello***************' 'world***************']

#####################################################################
arr = np.array(["hello", "world", "홍길동"])
s_encode = np.char.encode(arr,encoding="utf-8")
s_decode = np.char.decode(s_encode,encoding="utf-8")
print("11. encode: ", s_encode)  # [b'hello' b'world' b'\xed\x99\x8d\xea\xb8\xb8\xeb\x8f\x99']
print("12. decode: ", s_decode)  # ['hello' 'world' '홍길동']
#####################################################################
arr = np.array(["hello", "world", "홍길동"])
print("13. join", np.char.join(",",arr))
xxx = np.array([10,20,30], dtype=str)
xxx = np.arange(10).astype(str)
print("13. join", np.char.join(",",  xxx))
#print(",".join("hello")) # h,e,l,l,o
###########################################################
arr = np.array(["     hello     ", "     world     "])
print("14. lstrip", np.char.lstrip(arr)) #['hello     ' 'world     ']
print("14. rstrip", np.char.rstrip(arr)) #['     hello' '     world']
print("14. strip", np.char.strip(arr)) # ['hello' 'world']

arr = np.array(["HHHHhelloHHHH", "HHHworldAAAA"])
print("14. lstrip", np.char.lstrip(arr, "H" )) #['helloHHHH' 'worldAAAA']
print("14. rstrip", np.char.rstrip(arr, "H")) #['HHHHhello' 'HHHworldAAAA']
print("14. strip", np.char.strip(arr,"H")) # ['hello' 'worldAAAA']
#####################################################################
arr = np.array(["aaa bbb ccc", "world whoe dex"])
x, y = np.char.split(arr)
print("15. split: ", np.char.split(arr))  # [list(['aaa', 'bbb', 'ccc']) list(['world', 'whoe', 'dex'])]
print("15. split", x, y)  # ['aaa', 'bbb', 'ccc'] ['world', 'whoe', 'dex']

arr = np.array(["aaa/bbb/ccc", "world/whoe/dex"])
x, y = np.char.split(arr, "/")
print("15. split", x, y)  # ['aaa', 'bbb', 'ccc'] ['world', 'whoe', 'dex']
#####################################################################
arr = np.array(["John Hello my name is John"])
print("16. replace", np.char.replace(arr, "John", "Lee"))  # ['Lee Hello my name is Lee']
print("16. replace", np.char.replace(arr, "John", "Lee", count=1))  # ['Lee Hello my name is John']

#####################################################################
arr = np.array(["John Hello", "xxhere now"])
print("17. find", np.char.find(arr, 'n'))  # [3 7]
#####################################################################
arr = np.array(["John Hello", "xxhere now"])
print("18. count", np.char.count(arr, 'e'))  # [1 2]

#####################################################################
arr = np.array(["Hi", "he","His","She"])
print("19. startswith", np.char.startswith(arr, 'H'))  # [ True False  True False]
print("19. endswith", np.char.endswith(arr, 'e'))  # [False  True False  True]
#####################################################################
arr1 = np.array(["Hi", "he","His","She"])
arr2 = np.array(["Hi", "he","His","Sher"])
print("20. equal", np.char.equal(arr1, arr2))  # [ True  True  True False]
print("20. not_equal", np.char.not_equal(arr1, arr2))  # [False False False  True]
#####################################################################
arr = np.array(["HI", "he","His","88",99])
print(arr)  # ['Hi' 'he' 'His' '88' '99']
print("21. isalpha", np.char.isalpha(arr))  # [ True  True  True False False]
print("21. isdigit", np.char.isdigit(arr))  # [False False False  True  True]
print("21. isupper", np.char.isupper(arr))  # [ True False False False False]
print("21. islower", np.char.islower(arr))  # [False  True False False False]
#boolean 값으로 반환된 np.char.문자열함수는 boolean색인으로 활용 가능하다.
arr = np.array(["HI", "he","His","88",99])
print("대문자 출력:", arr[np.char.isupper(arr)])  # ['HI']