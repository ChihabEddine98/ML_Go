# Resolution & Refutation in PL 

# TD3 -- 16/02/2021
## Exo 3
1. $\{P,Q\}$
2. $\{P,\lnot Q\}$
3. $\{\lnot P, Q\}$
4. $\{\lnot P,\lnot Q\}$
5. $\{P\}$ **Res(1,2)**
6. $\{Q\}$ **Res(1,3)**
7. $\{\lnot P\}$ **Res(4,6)**
8. $\{\}$ **Res(5,7)** $\bot$

## Exo 4
### Q1
Let 
- $P$ 
- $\alpha_1 : P \rightarrow Q$ 
- $\alpha_2 : Q \rightarrow R$

$\alpha_1 \equiv \lnot P \lor Q$
$\alpha_2 \equiv \lnot Q \lor R$

So we have : 
1. $\{P\}$
2. $\{\lnot P,Q\}$
3. $\{\lnot Q,R\}$
4. $\{\lnot R\}$
5. $\{ Q \}$ **Res(1,2)**
6. $\{R\}$ **Res(3,4)** 
7. $\{\}$ **Res(4,6)** $\bot$

### Q2

1. $\{P,Q,R\}$
2. $\{\lnot P,R\}$
3. $\{\lnot Q\}$
4. $\{\lnot R\}$
5. $\{ R, Q \}$ **Res(1,2)**
6. $\{ R \}$ **Res(3,5)** 
7. $\{\}$ **Res(4,6)** $\bot$

### Q3 
1. $\{P,Q\}$
2. $\{\lnot Q,R\}$
3. $\{\lnot P,Q\}$
4. $\{\lnot R\}$
5. $\{ \lnot P, R \}$ **Res(2,3)**
6. $\{ R, Q\}$ **Res(1,5)**
7. $\{ R \}$ **Res(2,6)** 
8. $\{\}$ **Res(4,7)** $\bot$

### Q4
1. $\{A,\lnot B,\lnot C\}$
2. $\{\lnot A,C\}$
3. $\{\lnot E\}$
4. $\{A,B,E\}$
5. $\{\lnot C,\lnot E\}$
6. $\{ A, B,\lnot C\}$ **Res(4,5)**
7. $\{ A, \lnot C\}$ **Res(1,6)**
8. $\{ A ,\lnot A\}$ **Res(2,7)** $\blacksquare$