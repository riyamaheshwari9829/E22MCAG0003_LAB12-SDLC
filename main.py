import barbecue_sauce, marinara_sauce, plum_tomato_sauce, pumpkin_sauce
import reggiano_cheese, provolone_cheese, mozzarella_cheese, parmesan_cheese
import thin_crust_dough, thick_crust_dough
import chicago_pizza, sicilian_pizza, newyork_style_pizza, greek_pizza

def main():

    print('Riya Maheshwari  e22mcag0003')

    sauce_dict = {'1': plum_tomato_sauce.Plum_Tomato_Sauce(2), '2': marinara_sauce.Marinara_Sauce(4), '3': barbecue_sauce.Barbecue_Sauce(6), '4': pumpkin_sauce.Pumpkin_Sauce(8)}

    cheese_dict = {'1':mozzarella_cheese.Mozzarella_Cheese(3), '2':reggiano_cheese.Reggiano_Cheese(6), '3': provolone_cheese.Provolone_Cheese(9), '4':parmesan_cheese.Parmesan_Cheese(12)}

    dough_dict = {'1': thin_crust_dough.Thin_Crust_Dough(5), '2':thick_crust_dough.Thick_Crust_Dough(10)}

    p_choice = input('choose pizza type \n 01. Greek(7) \n 02. Chicago(10) \n 03. NewYork(5) \n 04. Sicilian(7)')
    s_choice = input('choose Sauce \n 01. PlumTomato(2) \n 02. Marinara(4) \n 03. Barbecue(2) \n 04. Pumpkin(4)')
    d_choice = input('choose Dough \n 01. ThinCrust(2) \n 02. ThickCrust(1)')
    c_choice = input('choose Cheese type \n 01. Mozzarella(2) \n 02. Reggiano(2) \n 03. Provolone(1) \n 04. Parmesan(4)')

    pizza = None
    if p_choice == '1':
        pizza = greek_pizza.Greek_Pizza(10, dough_dict[d_choice], cheese_dict[c_choice], sauce_dict[s_choice])
    elif p_choice == '2':
        pizza = chicago_pizza.Chicago_Pizza(20, dough_dict[d_choice], cheese_dict[c_choice], sauce_dict[s_choice])
    elif p_choice == '3':
        pizza = newyork_style_pizza.Newyork_Style_Pizza(30, dough_dict[d_choice], cheese_dict[c_choice], sauce_dict[s_choice])
    elif p_choice == '4':
        pizza = sicilian_pizza.Sicilian_Pizza(40, dough_dict[d_choice], cheese_dict[c_choice], sauce_dict[s_choice])
    else:
        print('wrong choice')
        

    print('Price of the requested Pizza: ',pizza.calculate_cost())
    pizza.print_details()
        
main()