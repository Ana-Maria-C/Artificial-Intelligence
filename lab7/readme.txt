
num_rows, num_cols:     Reprezintă numărul de rânduri și coloane ale mediului.
start_state:            Este starea de pornire a agentului în mediu.
goal_state:             Este starea țintă, adică starea în care agentul trebuie să ajungă.
wind:                   Este o listă ce indică efectul vântului pe fiecare coloană din mediul respectiv.
num_actions:            Numărul de acțiuni posibile pe care le poate lua agentul. Implicit, sunt 4 acțiuni: sus, dreapta, jos, stânga.
alpha:                  Rata de învățare pentru actualizarea Q-value-urilor (valorilor Q).
gamma:                  Factorul de discount pentru recompensele viitoare.
epsilon:                Probabilitatea de a alege o acțiune aleatoare în loc de a alege cea mai bună acțiune în funcția choose_action.
visited_states:         O lista cu stari vizitate pentru a evita intrarea in bucle in metoda take_action

choose-action:          o functie de explorare ce se bazeaza pe o strategie greedy
                        se alege o actiune random cu probabilitatea epsilon si actiunea cu valoare maxima pt starea Q cu probabilitate 1-epsilon
                        acesasta functie este folosita in algoritmul de invatare pentru explorarea starilor catre goal

update-table:           Actualizează valorile Q folosind rata de invatare alpha. Actualizează valoarea Q pentru o pereche stare-acțiune pe baza recompensei \
                        obținute și a estimării valorii Q pentru următoarea stare.

take-action:            Prin intermediul acțiunii date și a stării curente, calculează starea următoare și recompensa asociată.
                        Efectul vântului este luat în considerare în funcție de acțiunea și coloana actuală.
                        Verifică dacă starea următoare este una deja vizitată pentru a gestiona ciclurile și stabilește recompensa în funcție de
                        distanța față de starea țintă.

learning:               Implementează bucla de învățare a algoritmului Q-learning pentru un număr de episoade specificat.
                        Alege acțiuni, obține stări și recompense, actualizează valorile in tabela Q.

get_path:               Returnează un șir de stări care arată calea optimă sau cea obținută de algoritm pentru a ajunge de la starea inițială la starea țintă.
                        se foloseste de tabele Q
                        alege actiunea cu cea mai mare Qvaloare (starea cu cel mai mare reward)

policy:                 politica optimă (matricea de politici) în care fiecare celulă indică acțiunea optimă ce ar trebui luată într-o anumită stare.
                        din fiecre celula avem ce actiune trebuie facuta pentru parcurgerea optima:
                        0: Up
                        1: Right
                        2: Down
                        3: Left












Tabela Q: Aceasta este o tabelă tridimensională de dimensiunea num_rows x num_cols x num_actions, unde num_rows și num_cols reprezintă numărul de rânduri și coloane ale grilei, iar num_actions este numărul de acțiuni posibile. Fiecare element din tabelă, Q[i, j, k], reprezintă valoarea estimată a acțiunii k în starea (i, j). Valoarea este calculată pe baza recompenselor primite și a valorilor Q ale stărilor următoare. În timpul procesului de învățare, aceste valori sunt actualizate pentru a reflecta cunoștințele agentului despre mediul înconjurător.

Policy: Aceasta este o matrice bidimensională de dimensiunea num_rows x num_cols, unde fiecare element, policy[i, j], reprezintă acțiunea pe care agentul o va alege în starea (i, j) conform politicii curente. Politica este de obicei derivată din tabela Q prin alegerea acțiunii cu cea mai mare valoare Q pentru fiecare stare. În cazul tău, numerele din matricea policy reprezintă direcțiile de deplasare: 0 = sus, 1 = dreapta, 2 = jos, 3 = stânga.


