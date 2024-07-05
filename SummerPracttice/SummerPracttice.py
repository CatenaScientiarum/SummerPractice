
def backward_string(val: str) -> str:
    return val[::-1]
print("backward_string:")
print("Example:")
print(backward_string("val"))  # "lav"
print(backward_string("12"))  # "21"
print(backward_string("ohho"))  # "ohho"
print(backward_string("123456789"))  # "987654321"

print("")

def fizz(num: int) -> str:
    return "Fizz" if num % 3 == 0 else str(num)
print("Just Fizz!:")
print("Example:")
print(fizz(3))  # "Fizz"
print(fizz(15)) == "Fizz"
print(fizz(6)) == "Fizz"
print(fizz(10)) == "10"
print(fizz(7)) == "7"

print("")

def first_word(text: str) -> str:
    return text.split()[0]
print("First Word:")
print("Example:")
print(first_word("Hello world"))  # "Hello"
print(first_word("greeting from Ukraine"))  # "greeting"
print(first_word("a word"))  # "a"
print(first_word("hi"))  # "hi"

print("")

def rectangle_perimeter(length: int, width: int) -> int:
    return 2 * (length + width)
print("rectangle_perimeter")
print("Example:")
print(rectangle_perimeter(3, 2))  # 10
print(rectangle_perimeter(2, 4))  # 12
print(rectangle_perimeter(3, 5))  # 16
print(rectangle_perimeter(10, 20))  # 60
print(rectangle_perimeter(7, 2))  # 18

print("")

def determine_sign(num: int) -> str:
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"
print("determine_sign")
print("Example:")
print(determine_sign(11))  # "positive"
print(determine_sign(0))  # "zero"
print(determine_sign(-10))  # "negative"
print(determine_sign(1))  # "positive"
print(determine_sign(-1))  # "negative"
print(determine_sign(91))  # "positive"
print(determine_sign(123456789))  # "positive"
print(determine_sign(-987654321))  # "negative"



