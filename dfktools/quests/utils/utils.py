FAIL_ON_NOT_FOUND = False

types = {
    1: "attemptBased",
    #2: "timeBased",
    #3: "well",
}


def parse_type(id):
    value = types.get(id, None)
    if FAIL_ON_NOT_FOUND and value is None:
        raise Exception("Quest type not found")
    return value


def human_readable_quest(raw_quest):
    if raw_quest is None:
        return None

    quest = {}
    i = 0

    if len(raw_quest) == 10:  # v2
        quest['id'] = raw_quest[i]
        i = i + 1
        quest['address'] = raw_quest[i]
        i = i + 1
        quest['level'] = raw_quest[i]
        i = i + 1
        quest['heroes'] = raw_quest[i]
        i = i + 1
        quest['player'] = raw_quest[i]
        i = i + 1
        quest['startBlock'] = raw_quest[i]
        i = i + 1
        quest['startTime'] = raw_quest[i]
        i = i + 1
        quest['completeAtTime'] = raw_quest[i]
        i = i + 1
        quest['attempts'] = raw_quest[i]
        i = i + 1
        quest['type'] = parse_type(raw_quest[i])
    else:  # TODO:// v1 - remove once old quests have been migrated
        quest['id'] = raw_quest[i]
        i = i + 1
        quest['address'] = raw_quest[i]
        i = i + 1
        quest['heroes'] = raw_quest[i]
        i = i + 1
        quest['player'] = raw_quest[i]
        i = i + 1
        quest['startTime'] = raw_quest[i]
        i = i + 1
        quest['startBlock'] = raw_quest[i]
        i = i + 1
        quest['completeAtTime'] = raw_quest[i]
        i = i + 1
        quest['attempts'] = raw_quest[i]
        i = i + 1
        quest['type'] = parse_type(raw_quest[i])

    return quest