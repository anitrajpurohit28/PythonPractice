import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
# soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

# Method 1, to updated the stored shelve object
# with shelve.open('recipes') as recipes:
#     recipes["blt"] = blt
#     recipes["beans_on_toast"] = beans_on_toast
#     recipes["scrambled_eggs"] = scrambled_eggs
#     recipes["soup"] = soup
#     recipes["pasta"] = pasta
#
#     # even after appending few more to the list,
#     # recipes is not updated. Because in this method, only
#     # working copy is appended, which is not written back
#     recipes["blt"].append("butter")
#     recipes["pasta"].append("tomato")
#
#     # Method 1: To over come the write back problem, we
#     # can use the following method.
#     # Here something is assigned to dict element, which will be
#     # written back
#
#     # method 1
#     temp_list = recipes["blt"]
#     temp_list.append("butter")
#     recipes["blt"] = temp_list
#
#     temp_list = recipes["pasta"]
#     temp_list.append("tomota")
#     recipes["pasta"] = temp_list
#
#     recipes["soup"] = ["bowl of soup"]
#
#     for snack in recipes:
#         print(snack, recipes[snack])
#
# print("-"*20)

# # Method 2:
# # opening shelve with writeback option
# with shelve.open('recipes', writeback=True) as recipes:
#     recipes["blt"] = blt
#     recipes["beans_on_toast"] = beans_on_toast
#     recipes["scrambled_eggs"] = scrambled_eggs
#     recipes["soup"] = soup
#     recipes["pasta"] = pasta
#
#     # even after appending few more to the list,
#     # recipes is not updated. Because in this method, only
#     # working copy is appended, which is not written back
#
#     recipes["soup"].append("croutons")
#     recipes["blt"].append("butter")
#     recipes["pasta"].append("tomato")
#
#     for snack in recipes:
#         print(snack, recipes[snack])
#
# print("-"*20)


# # Method 3:
# # using dict's sync() method.
# # this does't seem to work

# with shelve.open('recipes') as recipes:
#     # recipes["blt"] = blt
#     # recipes["beans_on_toast"] = beans_on_toast
#     # recipes["scrambled_eggs"] = scrambled_eggs
#     # recipes["soup"] = soup
#     # recipes["pasta"] = pasta
#
#     # even after appending few more to the list,
#     # recipes is not updated. Because in this method, only
#     # working copy is appended, which is not written back
#
#     # method 2:
#     # using dict's sync() method.
#     recipes.sync()
#
#     recipes["soup"].append("croutons")
#     recipes["blt"].append("butter")
#     recipes["pasta"].append("tomato")
#
#     recipes.sync()
#
#     for snack in recipes:
#         print(snack, recipes[snack])
#
# print("-"*20)
# #
