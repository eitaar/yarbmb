from riichienv import Action, ActionType, Observation, calculate_shanten


class MyAgent:
    """Your bot agent. Implement act() to return an Action."""

    isRiichi = False

    def act(self, obs: Observation) -> Action:
        actions = obs.legal_actions()

        # Win if possible
        for a in actions:
            if a.action_type == ActionType.Tsumo or a.action_type == ActionType.Ron:
                print("----------\nWin\n----------")
                return a

        # Declare riichi if possible
        for a in actions:
            if a.action_type == ActionType.Riichi:
                self.isRiichi = True
                print("----------\nRiichi\n----------")
                return a

        discards = list(filter(lambda a: a.action_type == ActionType.Discard, actions))
        if self.isRiichi and discards:
            for a in discards:
                if a.tile == obs.drawn_tile:
                    print("Discarding: ", obs.drawn_tile)
                    print("----")
                    return a
        if not discards:
            return Action(ActionType.Pass)
        for a in discards:
            print("Discard Possible:", a.tile)

        print("My hand:", obs.hand)
        shantenList = []
        for i in range(len(obs.hand)):
            tmp = list(obs.hand)
            tmp.pop(i)
            shantenList.append(calculate_shanten(tmp))

        print(shantenList)
        discardTile = shantenList.index(min(shantenList))
        print("Discarding: ", obs.hand[discardTile])
        print("----")

        return Action(ActionType.Discard, obs.hand[discardTile])
