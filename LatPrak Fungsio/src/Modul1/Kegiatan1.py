# Penambahan

def tambah(kesatu, kedua):
    return kesatu+kedua

# Pengurangan


def minus(kesatu, kedua):
    return kesatu-kedua

# Perkalian


def mult(kesatu, kedua):
    return kesatu*kedua

# Pembagian


def div(kesatu, kedua):
    if kedua == 0:
        raise ValueError("Tidak dapat melakukan Pembagian Dengan nol")
    return kesatu/kedua


def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        operator, left_operand, right_operand = node
        if operator == '+':
            return tambah(tree(left_operand), tree(right_operand))
        elif operator == '-':
            return minus(tree(left_operand), tree(right_operand))
        elif operator == '*':
            return mult(tree(left_operand), tree(right_operand))
        elif operator == '/':
            return div(tree(left_operand), tree(right_operand))
    else:
        raise ValueError("Invalid expression tree node")

print("Kegiatan 1")
expression_tree = ('*', ('+', 2, 3), ('-', 5, 1))
result = tree(expression_tree)
print("Hasil Evaluasi Pohon Ekspresi:", result)
