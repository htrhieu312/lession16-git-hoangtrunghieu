def add(a: float, b: float) -> float:
    """Cộng hai số. Input: a, b (int/float). Output: tổng a + b."""
    return a + b


if __name__ == "__main__":
    print(add(2, 3))      # 5
    print(add(-1, 1))     # 0
    print(add(0.5, 0.25)) # 0.75