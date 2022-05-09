# 0003 : 状態遷移とモデル（状態）を持つエージェント
# 
# 人工知能開発では、代行者(agent)を作ります。
# 最も簡単なエージェントのモデルとして、入力に対する行動を返すエージェントを紹介します。
# 別名、オートマトン。システム設計では状態遷移図と言います。
# 特に、状態が有限（例えば、自販機の最大入金は1万円とする）ものを有限オートマトンと言います。
# 状態と入力から。出力を判断します。
#   input ∈ Input (入力の集合)
#   status ∈ Status（状態の集合）
#   action ∈ Action（行動の集合）
#   rule ∈ Rule (inputに対する、actionを書き下した集合)
#   agent ∈ Agent（エージェントの集合）
#
# モデル式： A = (I,S,A,R)
# モデル全体を内包するエージェントをモデルベースエージェントと呼びます。

class ModelBasedReflexAgent :

    status = 0
    
    def __init__(self) :
        self.status = 0

    def addCoin(self,coin) :
        if coin in [10,50,100,500] :
            if self.status + coin >= 990 : # 990円以上は投入できない自販機で、入れた効果がそのまま出てくる
                return [self.status,coin]
            else :
                self.status += coin
                return [self.status,0]
        else :
            return [self.status,coin] # 10円硬貨、50円硬貨、100円硬貨、500円硬貨意外は投入できない


mbrAgent = ModelBasedReflexAgent()
print(mbrAgent.addCoin(100))
print(mbrAgent.addCoin(300))
print(mbrAgent.addCoin(500))
print(mbrAgent.addCoin(500))


# 人工知能では、このモデルベースエージェントを基本にします。
# 状態とルールの管理を分かりやすくするためにオブジェクト指向が開発されました。
# 世界最初のオブジェクト指向言語はSmallTalkと言います。