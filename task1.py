

class EmailShielding:

    def __init__(self, shielding_symbol: str) -> None:

        if len(shielding_symbol) == 1:
            self.shielding_symbol = shielding_symbol
        else:
            raise Exception("Symbol must be the only one")

    def formating(self, emailinput: str) -> None:

        left,right = emailinput.split("@")[0], emailinput.split("@")[1]

        for i in range(len(left)):
            left = left.replace(left[i],self.shielding_symbol,1)
        format_email = left + "@" + right

        return format_email

class NumberShielding:

    def __init__(self, shielding_symbol: str, count_for_shielding: int = 3) -> None:

        if len(shielding_symbol) == 1:
            self.shielding_symbol = shielding_symbol
        else:
            raise Exception("Symbol must be the only one")

        self.count_for_shielding = count_for_shielding

    def normalize_number(self, number: str) -> str:

        normal_number = ""

        for i in number:
            if i.isdigit() or i == " ":
                normal_number += i

        return normal_number

    def formating(self, numberinput: str) -> str:

        number = self.normalize_number(numberinput)
        final_number = ""

        for i in range(len(number)-1, -1 , -1):

            if number[i].isdigit() and self.count_for_shielding != 0:
                final_number += self.shielding_symbol
                self.count_for_shielding -= 1
                continue

            if number[i] == " " and number[i-1] != " ":
                final_number += number[i]
                continue

            if self.count_for_shielding == 0 :
                final_number += number[i]


        return final_number[::-1]


class SkypeShielding:

    def __init__(self, shielding_symbol: str) -> None:

        if len(shielding_symbol) == 1:
            self.shielding_symbol = shielding_symbol
        else:
            raise Exception("Symbol must be the only one")

    def formatting(self, skypeinput: str):
        final_skype = ""
        i = 0
        length = len(skypeinput)
        while i < length:
            if skypeinput[i:i + 6] == 'skype:':
                final_skype += 'skype:xxx'
                i += 6

                while i < length and skypeinput[i] not in [',', '&', '?', '^', '/']:
                    i += 1
            else:
                final_skype += skypeinput[i]
                i += 1

        return final_skype
