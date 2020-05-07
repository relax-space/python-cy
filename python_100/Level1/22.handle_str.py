# 22.字符串的操作题目:
# 全字母短句 PANGRAM 是包含所有英文字母的句子，比如：A QUICK BROWN FOX JUMPS OVER THE LAZY DOG. 定义并实现一个方法 get_missing_letter, 传入一个字符串采纳数，返回参数字符串变成一个 PANGRAM 中所缺失的字符。应该忽略传入字符串参数中的大小写，返回应该都是小写字符并按字母顺序排序（请忽略所有非 ACSII 字符）
# 比如：
# (0)输入: "A quick brown fox jumps over the lazy dog"

# 返回： ""

# (1)输入: "A slow yellow fox crawls under the proactive dog"

# 返回: "bjkmqz"

# (2)输入: "Lions, and tigers, and bears, oh my!"

# 返回: "cfjkpquvwxz"

# (3)输入: ""

# 返回："abcdefghijklmnopqrstuvwxyz"



# 我之前的考虑是先把str看作是list，然后分别判断作为基准的字符PANGRAM中的在不在输入的str中，整的比较麻烦。
# 没有考虑过使用set
def get_missing_letter(input_str):
    PANGRAM = 'A QUICK BROWN FOX JUMPS OVER THE LAZY DOG'

    a = []
    for i in PANGRAM:
        if i not in input_str.upper():
            if i != ' ':
                a.append(i.lower())

    a = sorted(set(a))
    s =  ''.join(a)
    print(s)


# get_missing_letter('A slow yellow fox crawls under the proactive dog')

# 使用set非常简单
PANGRAM = 'A QUICK BROWN FOX JUMPS OVER THE LAZY DOG'
b = 'A slow yellow fox crawls under the proactive dog'

s = sorted(set(PANGRAM.lower()) - set(b.lower()))
s = ''.join(s)
print(s)





