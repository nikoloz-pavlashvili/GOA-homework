def sityva(sityvebi):
    if not sityvebi:
        return "" 

    sxva_sityva = sityvebi[0]

    for s in sityvebi:
        if len(s) > len(sityva):
            sxva_sityva = s

    return sxva_sityva

words = ["cotne", "nika", "dato", "goa"]
print(sityva(words))
