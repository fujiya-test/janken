import random

def janken():
    hands = ["グー", "チョキ", "パー"]
    print("じゃんけんをしましょう！")
    print("0: グー, 1: チョキ, 2: パー")
    
    try:
        player_hand = int(input("あなたの手を選んでください (0-2): "))
        if player_hand not in [0, 1, 2]:
            print("0, 1, 2 のどれかを入力してな！")
            return
            
        computer_hand = random.randint(0, 2)
        
        print(f"あなたの手: {hands[player_hand]}")
        print(f"コンピュータの手: {hands[computer_hand]}")
        
        if player_hand == computer_hand:
            print("あいこやな！")
        elif (player_hand == 0 and computer_hand == 1) or \
             (player_hand == 1 and computer_hand == 2) or \
             (player_hand == 2 and computer_hand == 0):
            print("あなたの勝ちや！おめでとう！")
        else:
            print("あなたの負けや... また挑戦してな！")
            
    except ValueError:
        print("数字を入れてクレメンス！")

if __name__ == "__main__":
    janken()
