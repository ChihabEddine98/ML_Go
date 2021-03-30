# TD8
## Exo 1
$\newcommand{\bb}{\mathbb}$
3.$\{Parents(x,father(x),mother(jane))\}$
$\{\lnot Parents(bill, father(y), mother(y))\}$ 
No possible unifier :  $\{x \lvert bill , y\lvert jane\}$

$P(x,y)$ : $x$ is $y$'s parent. 
$G(x,y)$ : $x$ is $y$'s grandparent. 
$\alpha :\forall x \forall y\forall z(P(x,y) \land P(y,z) )\rightarrow G(x,z)$
## Implication : 
$\alpha :\forall x \forall y\forall z\Big(\lnot(P(x,y) \land P(y,z) )\Big)\lor G(x,z)$
## Negation : 
$\alpha :\forall x \forall y\forall z\Big(\lnot P(x,y) \lor \lnot P(y,z) \Big)\lor G(x,z)$
## Universal : 
$\alpha : \Big(\lnot(P(x,y) \lor \lnot P(y,z) )\Big)\lor G(x,z)$
## Clauses  : 
$\{\lnot P(x,y) \lor \lnot P(y,z) \lor G(x,z)\}$

### Résolution : 

1. $\{A,\lnot B,\lnot C\}$
2. $\{\lnot A,C\}$
3. $\{\lnot E\}$
4. $\{A,B,E\}$
5. $\{\lnot C,\lnot E\}$
6. $\{ A, B,\lnot C\}$ **Res(4,5)**
7. $\{ A, \lnot C\}$ **Res(1,6)**
8. $\{ A ,\lnot A\}$ **Res(2,7)**

# TD7a

1. We need the rectangles as variables ( we can represent a rectangle with 2 points )
Just the top left $(x_1,y_1)$ and bottom right $(x_2,y_2)$
Check if 2 rect overlap : 
$$
