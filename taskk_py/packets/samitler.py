def Samitleri_al(cumle):
    samitler = []
    for i in cumle:
       if i.lower() in 'bcçdfgğhxjkqlmnprsştvyz' and i.lower() not in samitler:
        samitler.append(i.lower())
    return samitler