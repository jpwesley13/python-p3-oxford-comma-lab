def oxford_comma(items):
    if len(items) > 1:
        items[-1] = "and " + items[-1]
        # If there's more than one thing (2 things), then change the last thing from "thing" to "and thing."
    if len(items) > 2:
        return ", ".join(items)
    else:
        return " ".join(items)
    # If there're more than two things, do a comma plus space. Else if there are not more than two things (like if there are two things), do a space (which leads to "word[space]and[space]word2).