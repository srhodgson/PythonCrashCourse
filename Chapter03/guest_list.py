
guest_list = ['john smith', 'bob jones' ,'clive underwood']
message_one = f"Hi, {guest_list[0].title()} would you like to come to dinner?"
message_two = f"Hi, {guest_list[1].title()} would you like to come to dinner?"
message_three = f"Hi, {guest_list[-1].title()} would you like to come to dinner?"
print(message_one)
print(message_two)
print(message_three)

not_coming = f"Hi, {guest_list[0].title()} can't make the party"

print(not_coming)

guest_list.remove('john smith')

print(guest_list)

print()

guest_list.insert(0, 'brian redwood')

message_four = f"Hi, {guest_list[0].title()} would you like to come to dinner?"
message_five = f"Hi, {guest_list[1].title()} would you like to come to dinner?"
message_six = f"Hi, {guest_list[-1].title()} would you like to come to dinner?"
print(message_four)
print(message_five)
print(message_six)

print()


guest_list.insert(0, 'job stewart')
guest_list.insert(2, 'sarah sarah')
guest_list.append('billy lastname')

print(guest_list)

guest_list.pop()
print(guest_list)
guest_list.pop()
print(guest_list)
guest_list.pop()
print(guest_list)
guest_list.pop()
print(guest_list)
del guest_list[-1]
print(guest_list)
del guest_list[-1]
print(guest_list)