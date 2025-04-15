import re


# Загрузка инвертированного индекса из .txt-файла
def load_inverted_index(filepath):
    index = {}
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            if ':' in line:
                term, docs = line.strip().split(":", 1)
                index[term.strip()] = set(docs.strip().split())
    return index


# Преобразование булевого запроса в обратную польскую запись (RPN)
def to_rpn(query):
    precedence = {'NOT': 3, 'AND': 2, 'OR': 1}
    output = []
    stack = []

    tokens = re.findall(r'\w+|AND|OR|NOT|\(|\)', query)

    for token in tokens:
        token = token.upper()
        if token in {'AND', 'OR', 'NOT'}:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # убираем '('
        else:
            output.append(token.lower())

    while stack:
        output.append(stack.pop())
    return output


# Выполнение RPN-запроса
def evaluate_rpn(rpn, index, all_docs):
    stack = []
    for token in rpn:
        if token == 'NOT':
            operand = stack.pop()
            result = all_docs - operand
            stack.append(result)
        elif token in {'AND', 'OR'}:
            right = stack.pop()
            left = stack.pop()
            if token == 'AND':
                stack.append(left & right)
            else:
                stack.append(left | right)
        else:
            stack.append(index.get(token, set()))
    return stack[0] if stack else set()


# Основная функция
def boolean_search_interface(index_file):
    index = load_inverted_index(index_file)
    all_documents = set(doc for docs in index.values() for doc in docs)

    while True:
        query = input("\nВведите булев запрос (или 'exit' для выхода): ")
        if query.lower() == 'exit':
            break

        rpn = to_rpn(query)
        result_docs = evaluate_rpn(rpn, index, all_documents)

        print("Найдено документов:", len(result_docs))
        print("Документы:", sorted(result_docs))


# Пример использования
if __name__ == "__main__":
    boolean_search_interface("inverted_index.txt")
