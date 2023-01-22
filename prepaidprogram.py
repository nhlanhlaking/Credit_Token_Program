import random
import datetime

#This program is still under development; several functions are missing; nonetheless, it is capable of producing desired outcomes.



#Variables containing relevant list for pre-paid voucher
voucher = ["water", "airtime", "electricity"]
network = ["mtn", "vodacom", "cell c", "telkom"]

#The person who is attending the client
cashier_name = input("Cashier name: ")
cashier_surname = input("Cashier surname: ")
print("")
bold = "\33[1m"

#list of potential buyers of our pre-paid vourchers.
potential_buyers = ["Blessing Malehopo", "Bontle Lekgwathi", "Musa Sibiya", "Andile Mabuza", "Arnold Mabope", "Tiisetso Mokoena", "Lerato Bridgete Pule", "Olerato Bridgette Seemise", "Happy Phalane", "Nhlanhla Nhlapo", "Fanie Miya", "Nozipho Ngubane", "Koketso Marema", "Katlego Phoku", "Nqobile Zulu", "Lehlogonolo Maphari"]
name = random.choice(potential_buyers)
address = random.randint(1, 200)
meter_no = random.randint(10000000000, 99999999999)


#This is the function that executes all the transaction requested by the client and it is performed by the cashier.
def prepaidVoucher():
    print(voucher)
    print("")
    ans = input("Choose preferred voucher: ")
 

#Should the client request to purchase water credit token, this code will be executed.
    if ans == voucher[0]:   
        amount_of_kl = float(input("How many kilolitres: "))
        one_kilolitre_price = 14.27
        purchase_amount_water = one_kilolitre_price * amount_of_kl
        tax_water = 15.00 /  100.00 * purchase_amount_water
        grand_total = purchase_amount_water + tax_water
        pin = random.randint(10000000000000000000, 99999999999999999999)
        TodayDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print(">" * 56)
        print(f"{bold}" + " " * 15 + "JABULANI STREET SUPERMARKET")
        print(""); print("") 
        print("     Nhlanhla Nhlapo", "      Cel: +278 207 0553")
        print(""); print("-" * 55)
        print("Supplier: City of Tshwane Metropolitan Municipality")
        print(f"{address}  Savannah Country Estate")
        print(f"Customer:  {name}")
        print(f"Meter NO:  {meter_no}"); print("-" * 55)
        print("                    Water Token"); print("")
        print("TOTAL BEFORE VAT                         ", "R", "%.2f" % purchase_amount_water)
        print("TOTAL VAT                                ", "R", "%.2f" % tax_water)
        print("TOTAL AFTER VAT                          ", "R", "%.2f" % grand_total)
        print("")
        print(f'Congratulations you brought {"%.2f" % amount_of_kl} Kilolitres of water')
        print()
        print(f"PIN NO: {pin}"); print("-" * 55)
        print("")
        print("NO REFUNDS OR EXCHANGES ON CREDIT TOKEN"); print(TodayDate)
        print(f"You were helped by {cashier_name} {cashier_surname}")
        print(""); print(">" * 56)
        
        restart = input("Do you wish to start a new transaction: ").lower()
        if restart == "yes":
            prepaidVoucher()
        elif restart == "no":
            print("Thank you for supporting us")
            exit()
        else:
            print("You have entered invalid answer please restart the programme")
            exit() 
                   
            
#Should the client request to purchase airtime voucher, this code will be executed.            
    elif ans == voucher[1]:
        print(network)
        print("")
        network_ans = input("Choose preferred network: ")  
        
        if network_ans == network[0]:
            amount1 = float(input("Enter amount: "))
            TodayDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
            pin = random.randint(10000000000000000000, 99999999999999999999)
            
            print(">" * 56)
            print(f"{bold}" " " * 15 + "JABULANI STREET SUPERMARKET")
            print(""); print("")
            print("     Nhlanhla Nhlapo", "      Cel: +278 207 0553")
            print(""); print("-" * 55)
            print(f"Supplier:  {network_ans.upper()}")
            print("Adr: 2050 Block PP3, Shihlengwe Str", " Soshanguve")
            print("TAX Invoice NO", "   442 01 06777"); print("-" * 55)
            print("                    Airtime voucher"); print("")
            print("Amount                               ", "R", "%.2f" % amount1)
            print(""); print(f"PIN NO: {pin}"); print("-" * 55); print("")
            print("NO REFUNDS OR EXCHANGES ON CREDIT TOKEN"); print(TodayDate)
            print(f"You were helped by {cashier_name} {cashier_surname}")
            print(""); print(">" * 56)
            
            restart = input("Do you wish to start a new transaction: ").lower()
            if restart == "yes":
                prepaidVoucher()
            elif restart == "no":
                print("Thank you for supporting us")
                exit()
            else:
                print("You have entered invalid answer please restart the programme")
                exit() 
     
        
        elif network_ans == network[1]:
            amount1 = float(input("Enter amount: "))
            TodayDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
            pin = random.randint(10000000000000000000, 99999999999999999999)
            
            print(">" * 56)
            print(f"{bold}" " " * 15 + "JABULANI STREET SUPERMARKET")
            print(""); print("")
            print("     Nhlanhla Nhlapo", "      Cel: +278 207 0553")
            print(""); print("-" * 55)
            print(f"Supplier:  {network_ans.upper()}")
            print("Adr: 2050 Block PP3, Shihlengwe Str", " Soshanguve")
            print("TAX Invoice NO", "   442 01 06777"); print("-" * 55)
            print("                    Airtime voucher"); print("")
            print("Amount                               ", "R", "%.2f" % amount1)
            print(""); print(f"PIN NO: {pin}"); print("-" * 55); print("")
            print("NO REFUNDS OR EXCHANGES ON CREDIT TOKEN"); print(TodayDate)
            print(f"You were helped by {cashier_name} {cashier_surname}")
            print(""); print(">" * 56)
            
            restart = input("Do you wish to start a new transaction: ").lower()
            if restart == "yes":
                prepaidVoucher()
            elif restart == "no":
                print("Thank you for supporting us")
                exit()
            else:
                print("You have entered invalid answer please restart the programme")
                exit() 
        
            
            
        elif network_ans == network[2]:
            amount1 = float(input("Enter amount: "))
            TodayDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
            pin = random.randint(10000000000000000000, 99999999999999999999)
            
            print(">" * 56)
            print(f"{bold}" " " * 15 + "JABULANI STREET SUPERMARKET")
            print(""); print("")
            print("     Nhlanhla Nhlapo", "      Cel: +278 207 0553")
            print(""); print("-" * 55); print("Supplier: ", network_ans.upper())
            print("Adr: 2050 Block PP3, Shihlengwe Str", " Soshanguve")
            print("TAX Invoice NO", "   442 01 06777")
            print("-" * 55); print(" " * 20 + "Airtime voucher"); print("")
            print("Amount                               ", "R", "%.2f" % amount1)
            print("")
            print(f"PIN NO: {pin}"); print("-" * 55); print("")
            print("NO REFUNDS OR EXCHANGES ON CREDIT TOKEN"); print(TodayDate)
            print(f"You were helped by {cashier_name} {cashier_surname}")
            print(""); print(">" * 56)
            
            restart = input("Do you wish to start a new transaction: ").lower()
            if restart == "yes":
                prepaidVoucher()
            elif restart == "no":
                print("Thank you for supporting us")
                exit()
            else:
                print("You have entered invalid answer please restart the programme")
                exit() 
        
            
        elif network_ans == network[3]:
            amount1 = float(input("Enter amount: "))
            TodayDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
            pin = random.randint(10000000000000000000, 99999999999999999999)
            
            print(">" * 56)
            print(f"{bold}" " " * 15 + "JABULANI STREET SUPERMARKET")
            print(""); print(" ")
            print("     Nhlanhla Nhlapo", "      Cel: +278 207 0553"); print("")
            print("-" * 55)
            print(f"Supplier:  {network_ans.upper()}")
            print("Adr: 2050 Block PP3, Shihlengwe Str", " Soshanguve")
            print("TAX Invoice NO", "   442 01 06777")
            print("-" * 55); print(" " * 20 + "Airtime voucher"); print("")
            print("Amount                               ", "R", "%.2f" % amount1)
            print(""); print(f"PIN NO:  {pin}"); print("-" * 55); print("")
            print("NO REFUNDS OR EXCHANGES ON CREDIT TOKEN"); print(TodayDate)
            print(f"You were helped by {cashier_name} {cashier_surname}")
            print(""); print(">" * 56)
            
            restart = input("Do you wish to start a new transaction: ").lower()
            if restart == "yes":
                prepaidVoucher()
            elif restart == "no":
                print("Thank you for supporting us")
                exit()
            else:
                print("You have entered invalid answer please restart the programme")
                exit() 
        
                
#Should the client request to purchase electricity voucher, this code will be executed.          
    elif ans == voucher[2]:
        print("")
        purchase_amount_elec = float(input("Enter amount: "))
        tax_elec = 15 / 100 * purchase_amount_elec            
        municipal_charges = 10 / 100 * purchase_amount_elec
        total_before_vat_elec = purchase_amount_elec - (tax_elec + municipal_charges)
        unit_price = 1.50
        purchased_units = total_before_vat_elec / unit_price          
        pin = random.randint(10000000000000000000, 99999999999999999999)
        TodayDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        
        print(">" * 56)
        print(f"{bold}" " " * 15 + "JABULANI STREET SUPERMARKET")
        print(""); print("")
        print("     Nhlanhla Nhlapo", "      Cel: +278 207 0553")
        print(""); print("-" * 55)
        print("Supplier: City of Tshwane Metropolitan Municipality")
        print(f"{address} Savannah Country Estate")
        print(f"Customer:  {name}"); print(f"Meter NO:  {meter_no}"); print("-" * 55)
        print(" " * 18 + "Electricity Voucher"); print("")
        print("TOTAL BEFORE VAT                     ", "R", "%.2f" % total_before_vat_elec)
        print("TOTAL VAT                            ", "R", "%.2f" % tax_elec)
        print("MUNICIPAL CHARGES                    ", "R", "%.2f" % municipal_charges)
        print("GRAND TOTAL                          ", "R", "%.2f" % purchase_amount_elec)
        print(" ")
        print(f'Congratulations you brought {"%.2f" % purchased_units} kWh units')
        print(""); print(f"PIN NO: {pin}"); print("-" * 55); print("")
        print("NO REFUNDS OR EXCHANGES ON CREDIT TOKEN"); print(TodayDate)
        print(f"You were helped by {cashier_name} {cashier_surname}"); print(""); 
        print(">" * 56)  
        
        restart = input("Do you wish to start a new transaction: ").lower()
        if restart == "yes":
            prepaidVoucher()
        elif restart == "no":
            print("Thank you for supporting us")
            exit()
        else:
            print("You have entered invalid answer please restart the programme")
            exit()         
    else: 
        if ans != voucher:
            restart = input("You have entered invalid answer do wish to restart the programme? ").lower()
            if restart == "yes":
                prepaidVoucher()
            elif restart == "no":
                print("Thank you for supporting us")
                exit()
            else:
                print("You have entered invalid answer please restart the programme")
            exit() 
                          
prepaidVoucher()




