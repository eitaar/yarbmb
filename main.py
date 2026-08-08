import datetime
import json
import random

from riichienv import RiichiEnv

from yarbmb.agent import MyAgent

agent = MyAgent()
seed = random.randint(0, 100)
env = RiichiEnv(game_mode="4p-red-half", seed=seed)

observations = env.reset()


# ゲームが終了するまで繰り返す
while not env.done():
    # 現在行動する必要があるプレイヤーを処理する
    # for pid, obs in observations.items():
    #     # プレイヤー0なら手牌を表示する
    #     if pid == 0:
    #         print("My hand:", formatHand(obs.hand))

    # AIに行動を決めさせる
    actions = {pid: agent.act(obs) for pid, obs in observations.items()}

    # ゲームを1ステップ進める
    observations = env.step(actions)

print("Scores:", env.scores())
print("Ranks:", env.ranks())

filename = f"match_logs/{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
with open(filename, "w", encoding="utf-8") as f:
    for event in env.mjai_log:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")

print(f"Log saved to {filename}")
print("seed: ", seed)
