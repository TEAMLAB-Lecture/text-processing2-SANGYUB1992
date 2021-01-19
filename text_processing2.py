#######################
# Test Processing II  #
#######################


def digits_to_words(input_string):
    k=0
    digit_string = ''
    A=['zero ','one ','two ','three ','four ','five ','six ','seven ','eight ','nine ']
    for i in input_string:
        for j in range(10):
            if i==str(j):
                digit_string+=A[j]
                k=1
    if k==0:
        return ''
    return digit_string.strip()


"""
컴퓨터 프로그래밍에 많은 명명 규칙이 있지만, 두 규칙이 특히 흔히 쓰입니다. 
첫번째로는, 변수 이름을 'underscore'로 나눠준다거나, (ex. under_score_variable)
두번째로는, 변수 이름을 대소문자 구별해 구분자 (delimiter)없이 쓰는 경우가 있습니다. 
이 두번째의 경우에는 첫번째 단어는 소문자로, 그 후에 오는 단어들의 첫번째 글자들은 대문자로 쓰입니다 (ex. camelCaseVariable). 
"""


def to_camel_case(underscore_str):
    inn2=underscore_str.replace('_',' ')
    if inn2==underscore_str:
        return underscore_str
    camelcase_str = ''
    for index, value in enumerate(inn2.split()):
        if index==0:
            camelcase_str+=value.lower()
            continue
        camelcase_str+=value.capitalize()
    return camelcase_str
