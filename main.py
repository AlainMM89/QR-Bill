# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from qrbill import QRBill
import tempfile
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

# Press the green button in the gutter to run the script.


def create_reference(value):
    side_value = str(value) + str(271500)
    #print(side_value)
    modulo = int(side_value) % 97
    #print(modulo)
    checkDigits = 98 - modulo
    #print(checkDigits)

    if checkDigits < 10:
        return "RF0" + str(checkDigits) + str(value)

    return "RF" + str(checkDigits) + str(value)


if __name__ == '__main__':
    my_bill = QRBill(
        account='CH96 0483 5216 7077 3100 1',
        ref_number=create_reference("060122000001"),
        #ref_number="RF27 1332",
        creditor={'name': 'Marketingmonkeys GmbH', 'street': 'Wilstrasse 17', 'pcode': '4557', 'city': 'Horriwil', 'country': 'CH',},
        debtor={'name': 'Alain Habegger', 'street': 'Weiherweg 3', 'pcode': '3315', 'city': 'Bätterkinden', 'country': 'CH',},
        amount='0.10',
        language="de"
    )
    with tempfile.TemporaryFile(encoding='utf-8', mode='r+') as temp:
        my_bill.as_svg(temp)
        temp.seek(0)
        drawing = svg2rlg(temp)
        renderPDF.drawToFile(drawing, "file.pdf")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
