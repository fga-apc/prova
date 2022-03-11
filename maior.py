ns = [int(x) for x in input("ns: ").split(",")]

def maxarg(lst):
    max_pos = 0
    max_value = lst[0]
    
    for i, x in enumerate(lst):
        if x > max_value:
            max_value = x
            max_pos = i
        if not lst:
            return None
    return (max_pos, max_value)
pos, valor = maxarg(ns)
print(f"maior valor = {valor}, posicao = {pos + 1}°")
