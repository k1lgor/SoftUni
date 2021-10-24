easter_bread = int(input())
eggshell = int(input())
kg_cookies = int(input())

ttl_bread = easter_bread * 3.2
eggs = eggshell * 4.35
cookies = kg_cookies * 5.4
egg_paint = eggshell * 12 * 0.15

ttl = ttl_bread + eggs + cookies + egg_paint
print(f'{ttl:.2f}')