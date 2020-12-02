
def stats(data):
    stats = ''
    try:
        stats += '**+' + str(data["SimpleCombinedStatModifiers"]["Mastery"]) + '** Mastery\n'
    except Exception as e:
        pass
    try:
        #_endurance = _alacrity = str(data["SimpleCombinedStatModifiers"]["Endurance"])
        stats += '**+' + str(data["SimpleCombinedStatModifiers"]["Endurance"]) + '** Endurance\n'
    except Exception as e:
        pass
    try:
        stats += '**+' + str(data["SimpleCombinedStatModifiers"]["Power"]) + '** Power\n'
    except Exception as e:
        pass
    try:
        #_alacrity = str(data["SimpleCombinedStatModifiers"]["Alacrity Rating"])
        stats += '**+' + str(data["SimpleCombinedStatModifiers"]["Alacrity Rating"]) + '** Alacrity Rating\n'
    except Exception as e:
        pass
    try:
        #_accuracy = str(data["SimpleCombinedStatModifiers"]["Accuracy Rating"])
        stats += '**+' + str(data["SimpleCombinedStatModifiers"]["Accuracy Rating"]) + '** Accuracy Rating\n'
    except Exception as e:
        pass
    try:
        #_critical = str(data["SimpleCombinedStatModifiers"]["Critical Rating"])
        stats += '**+' + str(data["SimpleCombinedStatModifiers"]["Critical Rating"]) + '** Critical Rating\n'
    except Exception as e:
        pass
    if stats == '':
        stats = 'No stats!'
    return stats

def dColor(quality):

    if quality == 'Cheap':
        color = 0x979c9f
    elif quality == 'Premium':
        color = 0x00F200
    elif quality == 'Prototype':
        color = 0x1D8AFA
    elif quality == 'Artifact':
        color = 0xA335EE
    elif quality == 'Moddable':
        color = 0xE67E22
    elif quality == 'Legendary':
        color = 0x6105AD
    elif quality == 'Legacy':
        color = 0xE5CC80
    elif quality == 'Mission':
        color = 0xDEF700
    else:
        color = 0xFFFFFF
    return color

def durability(data):
    try:
        _durability = str(data["Durability"])
    except Exception as e:
        _durability = str(0)
    try:
        _max_durability = str(data["MaxDurability"])
    except Exception as e:
        _max_durability = str(0)
    return _durability +'/'+ _max_durability
