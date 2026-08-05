import datetime
import json

from riichienv import Action, Action3P, RiichiEnv

from yarbmb.agent import MyAgent

agent = MyAgent()
# Create a game environment
env = RiichiEnv(game_mode="4p-red-half", seed=42)
observations = env.reset()
while not env.done():
    # Collect actions from all players who need to act this turn
    actions: dict[int, Action | Action3P] = {
        pid: agent.act(obs) for pid, obs in observations.items()
    }
    observations = env.step(actions)
# Game finished — check results
print("Scores:", env.scores())
print("Ranks:", env.ranks())
# Full MJAI log is available
with open(
    f"match_logs/{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log", "w", encoding="utf-8"
) as f:
    for event in env.mjai_log:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")
