### Predicats : 
1. Dolphins are intelligent 
$D(x)$ : $x$ is a dolphin.
$I(x)$ : $x$ is intelligent 
$\forall x \; (D(x)\rightarrow I(x))$

2. Elena loves all animals.
$Elena $
3. Everyone Jack likes is liked by someone Nadia likes.
$a : Jack$
$b : Nadia$
$L(x,y)$ : $x$ likes $y$
$\forall x \; (L(a,x)\rightarrow \exists y  \; L(b,y) \land L(y,x))$
4. Among spiders, only tarantulas and black widows are poisonous.
$S(x)$ : $x$ is a spider
$T(x)$ : $x$ is tarantulas
$B(x)$ : $x$ is black widow 
$P(x)$ : $x$ is poisonous 
5. No sparrow builds a nest unless it has a mate.
6. Every prime number greater than 2 is odd.
7. There are pairs of primes numbers whose sum is prime.

## Exo 3
1. $\exists y \; \Bigg(G(y) \land \forall z \; \Big(R(z)\rightarrow P(y,z)\Big)\Bigg)$

## INEADOS : 
### Implications :
 $\exists y \; \Bigg(G(y) \land \forall z \; \Big(\lnot R(z)\lor P(y,z)\Big)\Bigg)$
### Existentiel :
 $\Bigg(G(a) \land \forall z \; \Big(\lnot R(z)\lor P(a,z)\Big)\Bigg)$
 ### Universal : 
 $\Bigg(G(y) \land  \Big(\lnot R(z)\lor P(y,z)\Big)\Bigg)$
### Distribution : 
$\Bigg(G(y) \land  \Big(\lnot R(z)\lor P(y,z)\Big)\Bigg)$
### Operators : 
Clauses are : 
$\{G(y)\}; \{\lnot R(z), P(y,z)\}$
### Standardize variables : 
Clauses are : 
$\{G(x)\}; \{\lnot R(z), P(y,z)\}$


2. Let 
$\alpha$: $\lnot \exists y \; \Bigg(G(y) \land \forall z \; \Big(R(z) \rightarrow P(y,z) \Big)\Bigg)$ 
And 
$\beta$: $\forall y \; \Bigg(\lnot G(y) \lor \exists z \; \Big(R(z) \land \lnot P(y,z) \Big)\Bigg)$ 
 Then
$\alpha \equiv \beta$

### Implications + Negation :
 $\forall y \; \Bigg(\lnot G(y) \lor \exists z \; \Big(R(z) \land \lnot P(y,z) \Big)\Bigg)$ 
### Existentiel :
$\forall y \; \Bigg(\lnot G(y) \lor \; \Big(R(f(y)) \land \lnot P(y,f(y)) \Big)\Bigg)$ 
 ### Universal : 
 $\Bigg(G(y) \land  \Big(\lnot R(z)\lor P(y,z)\Big)\Bigg)$
### Distribution : 
$\Bigg(G(y) \land  \Big(\lnot R(z)\lor P(y,z)\Big)\Bigg)$
### Operators : 
Clauses are : 
$\{G(y)\}; \{\lnot R(z), P(y,z)\}$
### Standardize variables : 
Clauses are : 
$\{G(x)\}; \{\lnot R(z), P(y,z)\}$
