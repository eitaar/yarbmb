from dataclasses import dataclass

from riichienv import Action, ActionType, Observation


@dataclass
class MyAgent:
    """Your bot agent. Implement act() to return an Action."""

    def act(self, obs: Observation) -> Action:
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
                return a
        # Pass on claims
        return Action(ActionType.Pass)
