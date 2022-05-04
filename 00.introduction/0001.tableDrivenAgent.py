# 0001 : 表形式のルールベースエージェント
# 
# 人工知能開発では、代行者(agent)を作ります。
# 最も簡単なエージェントのモデルとして、入力に対する行動を返すエージェントを紹介します。
# 別名、オートマトン。システム設計では状態遷移図と言います。
# その中でも、入力と出力のルールを全てルールで管理しているものを、Table Driven Agentと呼びます。
#   input ∈ Input (入力の集合)
#   action ∈ Action（行動の集合）
#   rule ∈ Rule (inputに対する、actionを書き下した集合)
#   agent ∈ Agent（エージェントの集合）
#
# モデル式： A = (I,A,R)
# 例：入力した硬貨がそのまま出てくる自動販売機

def table_driven_agent(input) :
    rule = {1:1,5:5,10:10,50:50,100:100,500:500}
    if input in rule.keys() :
        return rule[input]
    else :
        return "undefined"

print(table_driven_agent(5))
print(table_driven_agent(100))
print(table_driven_agent(400))
