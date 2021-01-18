class Luhn:
    def __init__(self, card_num):
        self.cleaned_card_num = []
        for char in card_num:
            if char in "0123456789":
                self.cleaned_card_num.append(int(char))
            elif char == " ":
                pass
            else:
                self.is_valid = False

        if len(self.cleaned_card_num) <= 1:
            self.is_valid = False

        if not hasattr(self, "is_valid") or self.is_valid != False:
            luhnd_nums = self.cleaned_card_num.copy()
            for num in range(-2, -1 - len(luhnd_nums), -2):
                doubled = self.cleaned_card_num[num] * 2
                if doubled > 9:
                    doubled = doubled - 9
                luhnd_nums[num] = doubled
            if sum(luhnd_nums) % 10 == 0:
                self.is_valid = True
            else:
                self.is_valid = False

    def valid(self):
        return self.is_valid


# luhn = Luhn("59")
luhn = Luhn("234 567 891 234")
print(luhn.valid())