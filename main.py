import rekins


def print_info():

    print('Invoicing program')

def lietotaja_ievade():
    print("\033[31m{}\033[0m".format("A bill is proposed legislation under consideration by a legislature.\n "
                                     "A bill does not become law until it is passed by the legislature and, in most cases, approved by the executive."))
    name = input('Ievadiet jūsu vārdu: ')
    tekst = input('Jūsu teksts:')
    size = float(input('Cik lielu kastīti jūs gribēsiet?(Cipari):'))
    height = float(input('Cik augstumā kastīti?:'))
    width = float(input('Cik platumā kastīti? (Cipari tikai): '))
    material = float(input('Materiāla cena'))
    length = float(input('Cik lielu garumu kastītei?'))

    darba_samaksa = 15
    PVN = 21

    produkta_cena = width/100.0 * length/100*height/100/3*material
    PVN_summa = produkta_cena + darba_samaksa * PVN / 100
    rekina_summa = produkta_cena + darba_samaksa + PVN_summa

    putin = [str(produkta_cena),str(PVN_summa), str(rekina_summa)]

    x=""
    y=[produkta_cena,PVN_summa,rekina_summa]
    write(x.join(y))
    print(lietotaja_ievade(y))

    f = open("rekins.txt", "w")
    f.write()
    f.close()

    print("Produkta cena: €" + format(produkta_cena, ",.2f"))
    print("PVN summa: €" + format(PVN_summa, ",.2f"))
    print("rekina_summa: €" + format(rekina_summa, ",.2f"))

from datetime import date

today = date.today()
print("Šodienas datums:", today)

if __name__ == '__main__':
    print_info()
    while True:
       lietotaja_ievade()
       restart = input('Gribēsiet vel reizi?(jā,nē) ').lower()
       if restart == "jā":
           print_info()
       else:
           break
