import networkx as nx


def string_count_with_char(s, c):
    count = 0
    s1 = s.lower()
    c_new = c.lower()
    s_new = s1.split()
    for i in s_new:
        if i[0] == c_new:
            count = count + 1
    return count


y = string_count_with_char("allo are you in there?", "A")
print y
