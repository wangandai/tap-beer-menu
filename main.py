import menu

m = menu.get_today_menu()
go_today, beers = menu.is_worth_going(m)

print(go_today)
print(beers)