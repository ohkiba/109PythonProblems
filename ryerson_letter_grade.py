def ryerson_letter_grade(pct):
    tens = pct // 10
    ones = pct % 10
    grade = ""

    if tens >= 8:
        grade = "A"
    elif tens >= 7:
        grade = "B"
    elif tens >= 6:
        grade = "C"
    elif tens >= 5:
        grade = "D"
    else:
        grade = "F"

    if 5 <= tens <= 7:
        if 7 <= ones <= 9:
            grade = grade + "+"
        if 3 <= ones <= 6:
            grade = grade + ""
        if 0 <= ones <= 2:
            grade = grade + "-"
    elif tens >= 8:
        if 5 <= ones <= 9:
            grade = grade + ""
        if 0 <= ones <= 4:
            grade = grade + "-"

    if pct >= 90:
        grade = "A+"

    return grade
