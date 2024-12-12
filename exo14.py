FRAME_WIDTH=30

word = input("Word: ")
word_length=len(word)

total_padding = FRAME_WIDTH - 2 - word_length
left_padding = total_padding // 2
right_padding = total_padding - left_padding

border = '*' * FRAME_WIDTH
middle = '*' + ' ' * left_padding + word + ' ' * right_padding + '*'

print(border)
print(middle)
print(border)