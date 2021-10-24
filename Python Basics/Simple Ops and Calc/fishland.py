mackerel_kg_price = float(input())
sprat_kg_price = float(input())
bonito_kg = float(input())
horse_mackerel_kg = float(input())
mussels_kg = int(input())

bonito_kg_price = mackerel_kg_price * 1.6
horse_mackerel_kg_price = sprat_kg_price * 1.8
ttl_mussels = mussels_kg * 7.5
ttl_bonito = bonito_kg * bonito_kg_price
ttl_horse_mackerel = horse_mackerel_kg * horse_mackerel_kg_price

print(f'{(ttl_mussels + ttl_bonito + ttl_horse_mackerel):.2f}')
