from riichienv import convert


def formatHand(hand: list[int]):
    formattedHand: dict[str, list[str]] = {"m": [], "p": [], "s": [], "z": []}
    mpsz_list = convert.tid_to_mpsz_list(hand)
    for mpsz in mpsz_list:
        formattedHand[mpsz[1]].append(mpsz[0])
    for key in ["m", "p", "s", "z"]:
        formattedHand[key].sort()
    return "".join(
        [
            "".join(formattedHand["m"]) + "m" if formattedHand["m"] else "",
            "".join(formattedHand["p"]) + "p" if formattedHand["p"] else "",
            "".join(formattedHand["s"]) + "s" if formattedHand["s"] else "",
            "".join(formattedHand["z"]) + "z" if formattedHand["z"] else "",
        ]
    )
