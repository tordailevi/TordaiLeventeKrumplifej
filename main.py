import regisztracio
import sorozat
import megrendelok

'''regisztracio.feladat1()
randomszamok = sorozat.feladat2()
szamlalo = sorozat.nagyobb(randomszamok)
sorozat.konzol_ir(szamlalo)
sorozat.fajba_ir(szamlalo)'''
megrendeles_lista = megrendelok.filebeolvasas()
megrendelok.rendelesszam(megrendeles_lista)
megrendelok.krumplifej(megrendeles_lista)
megrendelok.legutolso_rendeles(megrendeles_lista)