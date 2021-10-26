needed_exp, battles = float(input()), int(input())

ttl_exp = 0

for battle in range(1, battles + 1):
    
    exp_battle = float(input())
    ttl_exp += exp_battle
    
    if battle % 3 == 0:
        ttl_exp += exp_battle * 0.15
    if battle % 5 == 0:
        ttl_exp -= exp_battle * 0.10
    if battle % 15 == 0:
        ttl_exp += exp_battle * 0.05
    if ttl_exp >= needed_exp:
        print(f"Player successfully collected his needed experience for {battle} battles.")
        break
    
if ttl_exp < needed_exp:
    print(f"Player was not able to collect the needed experience, {(needed_exp - ttl_exp):.2f} more needed.")
        