from dataclasses import dataclass

from riichienv import Action, ActionType, Observation, calculate_shanten


@dataclass
class MyAgent:
    """Your bot agent. Implement act() to return an Action."""

    def act(self, obs: Observation, pid: int) -> Action:
        actions = obs.legal_actions()

        # 1. Win if possible
        for a in actions:
            if a.action_type == ActionType.Tsumo or a.action_type == ActionType.Ron:
                print("Winning...")
                return a

        # 2. Declare riichi if possible
        for a in actions:
            if a.action_type == ActionType.Riichi:
                print("Declaring riichi...")
                return a

        # 3. Discard the tile that minimizes shanten
        discards = [a for a in actions if a.action_type == ActionType.Discard]
        if discards:
            hand = list(obs.hand)
            shanten_list = [calculate_shanten(hand[:i] + hand[i + 1 :]) for i in range(len(hand))]
            best = shanten_list.index(min(shanten_list))

            if pid == 0:
                print("My hand:", hand)
                print("Shanten per discard:", shanten_list)
                print("Discarding:", hand[best])
                print("----")

            return Action(ActionType.Discard, hand[best])

        # 4. Reaction phase: pass
        for a in actions:
            if a.action_type == ActionType.Pass:
                return a

        return Action(ActionType.Pass)
