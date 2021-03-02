
-- BDD model : 
/*
-- Produit (constructeur, modele, type)
-- Pc (modele, vitesse, ram, hd, cd, prix)
-- Portable (modele, vitesse, ram, hd, ecran, prix)
-- Imprimante (modele, couleur, type, prix)
*/



-- Question 01 :
-- Quels sont les portables (laptop en anglais) référencés dans la relation Produits ? 
SELECT modele FROM Produit WHERE type="laptop";

-- Question 02 :
-- Quelle est la liste des constructeurs ?
SELECT DISTINCT constructeur FROM Produit;

-- Question 03:
-- Quels sont les modèles des ordinateurs référencés ?
SELECT modele FROM Produit WHERE type in ("Desktop","Laptop");

-- Question 04 :
-- Quels sont les PC avec 256 Mo de RAM ?
SELECT * FROM Pc WHERE ram=256;

-- Question 05 :
-- Quels sont les PC à exactement moins de 1100 Euros ?
SELECT * FROM Pc WHERE prix < 1100;

-- Question 06
-- Quels sont les portables avec un disque d’au moins (ou égal à) 50 Go et à moins de
-- (ou égal à) 1400 Euros ?
SELECT * FROM Portable WHERE hd >= 50 AND prix <= 1400;

-- Question 07
-- Quelles sont les imprimantes laser couleur ?
SELECT * FROM Imprimante WHERE couleur=TRUE AND type="laser";

-- Question 08
-- Quels sont les portables du constructeur D ayant au moins 256 Mo de RAM ?
SELECT * FROM Portable as tel JOIN Produit as p ON (p.modele = tel.modele)
WHERE pr.constructeur = "D" AND tel.ram = 256;

-- Question 09
-- Quels sont les ordinateurs du constructeur D ayant au moins 256 Mo de RAM ?

-- Question 10
-- Quels sont les ordinateurs coûtant exactement moins de 1200 Euros ?


-- Question 14
-- Quels sont les constructeurs ne fournissant qu’un type de materiel ?
Select Constructeur From Produit EXCEPT 
(Select Constructeur FROM Produit Where Type = 'laptop' OR Type='Printer')
UNION
Select Constructeur From Produit EXCEPT
(Select Constructeur FROM Produit Where Type = 'Desktop' OR Type='Printer')
UNION
Select Constructeur From Produit EXCEPT 
(Select Constructeur FROM Produit Where Type = 'Desktop' OR Type='Laptop') ;

-- TODO
-- Try Difficulty level 3