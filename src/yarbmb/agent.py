from dataclasses import dataclass

from riichienv import Action, ActionType, Observation


@dataclass
class MyAgent:
    """Your bot agent. Implement act() to return an Action."""

    def act(self, obs: Observation, pid: int) -> Action:
        actions = obs.legal_actions()

        # Win if possible
        for a in actions:
            if a.action_type == ActionType.Tsumo or a.action_type == ActionType.Ron:
                return a
        # Declare riichi if possible
        for a in actions:
            if a.action_type == ActionType.Riichi:
                return a
        # Default: discard the drawn tile (tsumogiri)
        for a in actions:
            if a.action_type == ActionType.Discard:
                # print("My hand:", formatHand(obs.hand))
                # print("Discarding:", formatHand([a.tile]))
                if pid == 0:
                    print("My hand:", obs.hand)
                    print("Discarding:", a.tile)
                    print("----")
                return a
        # Pass on claims
        return Action(ActionType.Pass)
