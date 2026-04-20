import random

def get_hand_name(hand_index):
    hands = ["グー", "チョキ", "パー"]
    return hands[hand_index]

def play_round():
    print("\n0: グー, 1: チョキ, 2: パー")
    try:
        player_hand = int(input("あなたの手を選んでください (0-2): "))
        if player_hand not in [0, 1, 2]:
            print("0, 1, 2 のどれかを入力してな！")
            return None
            
        computer_hand = random.randint(0, 2)
        
        print(f"あなたの手: {get_hand_name(player_hand)}")
        print(f"コンピュータの手: {get_hand_name(computer_hand)}")
        
        if player_hand == computer_hand:
            print("あいこやな！")
            return "draw"
        elif (player_hand == 0 and computer_hand == 1) or \
             (player_hand == 1 and computer_hand == 2) or \
             (player_hand == 2 and computer_hand == 0):
            print("このラウンドはあなたの勝ちや！")
            return "player"
        else:
            print("このラウンドはあなたの負けや...")
            return "computer"
            
    except ValueError:
        print("数字を入れてクレメンス！")
        return None

def janken():
    print("じゃんけんをしましょう！")
    print("1: 通常モード (1回勝負)")
    print("2: さんまモード (3回先取)")
    
    mode = input("モードを選んでください (1 or 2): ")
    
    target_wins = 3 if mode == "2" else 1
    player_wins = 0
    computer_wins = 0
    
    if target_wins == 3:
        print("\n--- さんまモード（3回先取）開始！ ---")
    else:
        print("\n--- 通常モード（1回勝負）開始！ ---")

    while player_wins < target_wins and computer_wins < target_wins:
        result = play_round()
        if result == "player":
            player_wins += 1
        elif result == "computer":
            computer_wins += 1
        
        if target_wins > 1:
            print(f"現在のスコア - あなた: {player_wins}, コンピュータ: {computer_wins}")

    if player_wins == target_wins:
        print("\n最終結果: あなたの勝ちや！おめでとう！")
    else:
        print("\n最終結果: あなたの負けや... また挑戦してな！")

if __name__ == "__main__":
    janken()
