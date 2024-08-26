calls = 0
def count_calls():
    global calls
    calls += 1


def string_info(string_):
    count_calls()
    n = len(string_)
    m = string_.upper()
    q = string_.lower()
    return n, m, q


i = string_info("rumpelshtirltzhen")
print(i)
i = string_info("demobilizacya")
print(i)

s = "urban"
l = ["potato", "tomato", "URBAN"]

def is_contains(s, l):
    count_calls()
    if s.lower() in (item.lower() for item in l):
        print(True)
    else:
        print(False)


is_contains(s, l)
print(calls)


