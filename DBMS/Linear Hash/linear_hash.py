




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

    def insert(self , v):
        pos = self.trouvePosition(v)
        new_page_pos = [None]*2

        print(self.pages)
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

            self.p += 1

            if self.p == self.M:
                self.p = 0
                self.doublements += 1
                self.M *= 2
                self.pages.append([self.new_page()])














if __name__ == '__main__':
    h = LH(2,3)

    h.show()
    h.insert(4)
    h.insert(8)
    h.insert(16)
    h.insert(2)
    h.insert(18)


    h.show()