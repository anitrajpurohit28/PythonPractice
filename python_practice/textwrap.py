# Text Wrap

import textwrap

input_str = "qwertyuiopsdfghjklzxcvbnm"
max_width = 3

wrapper = textwrap.TextWrapper(width=7)
# This returns a list
print("\nwrapper.wrap")
word_list = wrapper.wrap(text=input_str)
print(word_list)
# for each_line in word_list:
#     print(each_line)

# This returns a string will multiline output,
# with max len of line mentioned in width
new_str = wrapper.fill(input_str)
print(new_str)

input_str2 = """\
                Hello
                    World
            """
print("\ntextwrap.dedent")
print("Original:")
print(repr(input_str2))
dedented_txt = textwrap.dedent(input_str2)
print("Dedented:")
print(repr(dedented_txt))


input_str3 = """This function wraps the input paragraph such that each line 
n the paragraph is at most width characters long. The wrap method 
returns a list of output lines. The returned list 
is empty if the wrapped 
output has no content."""

print("\ntextwrap.shorten")
print("Original:\n", input_str3)
print()
print("Shorened:\n", textwrap.shorten(input_str3, width= 50))

print("\ntextwrap.indent")
input_str4 = "Hello\nWorld"
print("Original:\n", input_str4)
res1 = textwrap.indent(text=input_str4, prefix='+')
print("indent:\n", res1)

input_str = "qwertyuiopsdfghjklzxcvbnm"
max_width = 8

print("\nText wrap")
def wrap_str_split(string, max_width):
    res = "\n".join(string[i: i+max_width] for i in range(0, len(string), max_width))
    return res

def wrap_TextWrapper(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    dedented_text = textwrap.dedent(text=string)
    result = wrapper.fill(text=dedented_text)
    return result


res = wrap_str_split(input_str, max_width)
print(res)

res = wrap_TextWrapper(input_str, max_width)
print(res)


#     import textwrap
#     S = input()
#     w = input()
#     print(textwrap.fill(S,  w))

