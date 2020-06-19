#Ch3. Recursive
# 1
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            else item.is_a_key():
                print("열쇠를 찾았어요!")

# 2
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)          # 반복
        else item.is_a_key():
            print("열쇠를 찾았어요!")
