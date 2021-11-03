[check this link](https://www.math.cmu.edu/~wgunther/talks/modallogic.pdf)
and [this links](https://formal.kastel.kit.edu/~beckert/teaching/Spezifikation-SS04/04ModalLogic.pdf) 
[, and this Book](https://builds.openlogicproject.org/courses/boxes-and-diamonds/bd-screen.pdf)
## Exo 1.
---
- Let $\mathcal{W}_i$ be the set of worlds satisfying $\phi_i$ 
1. If $\phi_1 : P$  then $\mathcal{W}_1 = \{w,s\}$
2. IF $\phi_2 : \square P$  then $\mathcal{W}_2 = \{u,w,s\}$
3. IF $\phi_3 : \Diamond\square P$  then $\mathcal{W}_3 = \{u,v,w\}$
4. IF $\phi_4 : q\rightarrow p$  then $\mathcal{W}_4 = \{v,w,s\}$
5. IF $\phi_5 : \square (q\rightarrow p)$  then $\mathcal{W}_4 = \{w,s,u\}$

## Exo 2.
---
1. $\square$ doesn't distribute over $\lor$ : 
    - $w_0 \models \square\;(\lnot p \lor \lnot p)$
    - $w_0 \not\models \square\;\lnot p \lor \square\;\lnot p$
2. $\Diamond$ doesn't distribute over $\land$ : 
    - $w_0 \models \Diamond\;(p \land  q)$
    - $w_0 \not\models \Diamond\; p \land \Diamond\;q$


## Exo3. 
---
- Proof that $\Big (\square\; (\varphi \rightarrow \psi) \land \square\; \varphi \Big )\rightarrow \Big ( \square\;\psi\Big ) $ is valid :

- Let $\mathcal{M} =(\mathcal{W},\mathcal{R},V)$ any 'Kripke'-model and assume that there exists a world $w$ **s.t** :  $M,w$ $\models$ $\square\; (\varphi \rightarrow \psi) \land \square\; \varphi$

$M,w \models \square\; (\varphi \rightarrow \psi) \land \square\; \varphi$

$M,w \models \square\; (\varphi \rightarrow \psi)$ **and** 
$M,w \models  \square\; \varphi$  

means that for all worlds $w'$ **s.t:**
$w\mathcal{R}w'$ ($w'$ accesible from $w$) **We have** 
$M,w' \models\; \varphi \rightarrow \psi$ **and** 
$M,w' \models \varphi$
Applying the Modus-Poenus here we get exactly what expected.