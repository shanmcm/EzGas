#Search by address and evaluate prices of a gas station as wrong
type("1590681811380-1.png", "Via Magenta 52/D Turin Piemont")
wait("gs_list2-1.png")
click("item2-1.png")
click("1590682218881-1.png")
wait("1592405322338.png")
type(Key.PAGE_DOWN)
wait("1592405348923.png")
region = (Region(210,631,1475,158))
click(region.inside().find("1590682681410.png"))