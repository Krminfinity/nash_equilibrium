import pandas as pd
import numpy as np
import nashpy as nash

# Excelファイルからデータを読み込みます
input_file = 'game_input.xlsx'
sheet_name = 'GameData'

# データを読み込む
df = pd.read_excel(input_file, sheet_name=sheet_name, header=None)

# プレイヤーの戦略を取得
player1_strategies = df.loc[df[0] == 'Player1_Strategies', 1].values[0].split(',')
player2_strategies = df.loc[df[0] == 'Player2_Strategies', 1].values[0].split(',')

num_strategies_p1 = len(player1_strategies)
num_strategies_p2 = len(player2_strategies)

# プレイヤー1の利得行列を取得
payoff_p1_start = df.index[df[0] == 'Payoff_Matrix_P1'][0] + 2
payoff_p1_end = payoff_p1_start + num_strategies_p1
payoff_matrix_p1 = df.iloc[payoff_p1_start:payoff_p1_end, 1:1+num_strategies_p2].values.astype(float)

# プレイヤー2の利得行列を取得
payoff_p2_start = df.index[df[0] == 'Payoff_Matrix_P2'][0] + 2
payoff_p2_end = payoff_p2_start + num_strategies_p1
payoff_matrix_p2 = df.iloc[payoff_p2_start:payoff_p2_end, 1:1+num_strategies_p2].values.astype(float)

# ゲームを定義
game = nash.Game(payoff_matrix_p1, payoff_matrix_p2)

# 混合戦略ナッシュ均衡を計算
equilibria = list(game.support_enumeration())

# 結果をDataFrameにまとめる
results = []

for eq in equilibria:
    sigma_r, sigma_c = eq
    result = {}
    for strategy, prob in zip(player1_strategies, sigma_r):
        result[f'Player1_{strategy}'] = prob
    for strategy, prob in zip(player2_strategies, sigma_c):
        result[f'Player2_{strategy}'] = prob
    results.append(result)

results_df = pd.DataFrame(results)

# 結果をExcelファイルに出力
output_file = 'game_output.xlsx'
results_df.to_excel(output_file, index=False)

print(f"混合戦略ナッシュ均衡の計算が完了しました。結果は '{output_file}' に出力されています。")
