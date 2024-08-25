calls = 0
def count_calls():
    print(calls)

def string_info(string_):
    global calls
    calls += 1
    n = len(string_)
    m = string_.upper()
    q = string_.lower()
    return n, m, q


i = string_info("proba")
print(i)
i = string_info("demobilizacya")
print(i)

s = "urban"
l = ["potato", "tomato", "URBAN"]

def is_contains(s, l):
    global calls
    calls += 1
    if s.lower() in (item.lower() for item in l):
        print(True)
    else:
        print(False)


is_contains(s, l)


count_calls()