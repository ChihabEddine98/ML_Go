




class LH:
    def __init__(self, M, dpag):
        self.M = M
        self.dpag = dpag
        self.p = 0
        self.doublements = 1

        self.pages = [[[None] * self.dpag] for x in range(M)]

    def show(self):

        print("M: ", self.M)
        print("dpage: ", self.dpag)
        print("p: ", self.p)
        print("doublements: ", self.doublements)
        print("pages:")

        for x in self.pages: print(x)

    def trouvePosition(self, v):

        m = v % (self.M * (2**(self.doublements -1)))

        if m >= self.p:
            return m
        else:
            return v % ( self.M * (2** self.doublements))

    def new_page(self):
        return [None]* self.dpag

    def insertionDansChaine(self, v, position):

        pageEtIndex = [None, None]

        # On parcourt les pages de la chaine pour trouver une place

        for x in range(len(self.pages[position])):

            if None in self.pages[position][x]:

                pageEtIndex[1] = self.pages[position][x].index(None)

                pageEtIndex[0] = x

            break

        # Si il y a une place on met v à cette place

        if pageEtIndex[0] is not None:
            self.insertionSurPosition(v, position, pageEtIndex)
            return False

        # Sinon on rajoute une page dans la chaine (ce qui va provoquer un debordement +repartition).

        else:
            self.pages[position].append([None] * self.dpag)
            pageEtIndex[1] = 0
            pageEtIndex[0] = -1
            self.insertionSurPosition(v, position, pageEtIndex)
            return True

    def insert(self , v):
        pos = self.trouvePosition(v)
        new_page_pos = [None]*2

        for i in range(len(self.pages[pos])):
            if None in self.pages[pos][i]:
                new_page_pos = [i,self.pages[pos][i].index(None)]


        if new_page_pos[0] is not None:
            self.pages[pos][new_page_pos[0]][new_page_pos[1]] = v
        else: # Y a débordement
            new_page = self.new_page()
            self.pages[pos].append(new_page)
            new_page_pos = [-1, 0]
            self.pages[pos][new_page_pos[0]][new_page_pos[1]] = v



            if self.p == self.M:
                self.p = 0
                self.doublements += 1
                self.M *= 2
                self.pages.append([self.new_page()])
            else :
                self.p += 1















if __name__ == '__main__':
    h = LH(2,2)

    h.show()
    for i in range(1,10):
        h.insert(i)
        h.show()


    h.show()