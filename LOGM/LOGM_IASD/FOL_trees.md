## Exo 1 : (Translations)
---
1. $\alpha_1$ :  Brenda likes Anne if and only if Anne is not taller than Brenda. 

- Let $a = Anne$ ,  $b = Brenda$
- Let $T(x,y)$ : "$x$ is taller than $y$"
- Let $L(x,y)$ : "$x$ likes $y$"

$$
 \alpha_1 : \;  L(b,a) \leftrightarrow \neg \; T(a,b)
$$

2. $\alpha_2$ :  Anne likes everyone Brenda likes. 

- Let $a = Anne$ ,  $b = Brenda$
- Let $L(x,y)$ : "$x$ likes $y$"

$$
 \alpha_2 : \;  \forall x \; ( L(b,x) \rightarrow L(a,x))
$$

3. $\alpha_3$ : Carl likes everyone who likes him.

- Let $c = Carl$
- Let $L(x,y)$ : "$x$ likes $y$"

$$
 \alpha_3 : \;  \forall x \; L(x,c) \rightarrow L(c,x)
$$

4. $\alpha_4$ : Brenda likes somebody who likes her.

- Let $b = Brenda$
- Let $L(x,y)$ : "$x$ likes $y$"

$$
 \alpha_4 : \;  \exists x \; L(x,b) \land L(b,x)
$$

5. $\alpha_5$ : Everybody likes somebody.

- Let $L(x,y)$ : "$x$ likes $y$"

$$
 \alpha_5 : \;  \forall x  \; \exists y \; L(x,y)
$$

6. $\alpha_6$ : There is someone everyone likes.

- Let $L(x,y)$ : "$x$ likes $y$"

$$
 \alpha_6 : \;  \exists x  \; \forall y \; L(y,x)
$$

7. $\alpha_7$ : All fish but angler fish are cute.

- Let $F(x)$ : $x$ is a fish
- Let $A(x)$ : $x$ is an angler fish
- Let $C(x)$ : "$x$ is cute ☺️"

$$
 \alpha_7: \;  \forall x\; \big ( (F(x) \land \neg A(x)) \rightarrow C(x) \big )
$$

8. $\alpha_8$ : You can fool some people sometime but you cannot fool everybody all the time.

- Let $F(x,t)$ : " You fool $x$ at time $t$ 😡"

$$
 \alpha_8: \;  (\exists x\;\exists t\; F(x,t)) \land \neg (\forall x' \forall t' F(x',t')) 
$$

## Exo 2. (Tree Procédure for FOL)
---

I) $\Gamma_1 = \{ \forall x\exists yF(x,y) , G(a)\land \neg \exists y F(a,y)\}$

#### Hypothesis 
1. $\forall x\exists yF(x,y)$ 
2. $G(a)\land \neg \exists y F(a,y)$
---
3. $G(a)$ [$R_{\land , 2}$]
4. $\neg \exists y F(a,y)$ [$R_{\land , 2}$]
5. $\exists yF(a,y)$ [$R_{\forall , 1}$]
6. $\bigotimes$

II) $\Gamma_2 = \{ \exists yG(y)\rightarrow \forall x F(x,b) , \exists z \neg F(z,b)\}$
#### Hypothesis 
1. $\exists yG(y)\rightarrow \forall x F(x,b)$
2. $\exists z \neg F(z,b)$
---
3. 