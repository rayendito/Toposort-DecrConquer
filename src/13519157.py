#ENEM : Program Pemilihan Rencana Studi
#Ryandito Diandaru 
#13519157
#K03

#class node matkul
class matkul:
    def __init__(self, raw):#inisialisasi node matkul
        self.name = raw[0]              #nama matkul
        self.prereq = raw[1:len(raw)]   #nama-nama matkul prerequisite
        self.inDegree = len(raw)-1      #jumlah derajat masuk
    
    def changeInDegree(self, n):#method mengubah indegree
        self.inDegree += n

#class graph
class graph:
    def __init__(self):#inisialisasi graph
        self.nodes = []

    #menambah node yang berupa objek matkul
    def addNode(self, nod):
        self.nodes.append(nod)

    #menghilangkan course dari graph, asumsi matkul sudah diambil
    def popNode(self, nod):
        for i in range(len(self.nodes)):
            #mengambil indeks dari matkul yang akan dihiilangkan dari graph
            if(self.nodes[i].name == nod.name):
                todelete = i
            #mengurangi in degree dari matkul matkul yang
            #menjadikan matkul sekarang prereq
            if (nod.name in self.nodes[i].prereq):
                self.nodes[i].changeInDegree(-1)
        #mendelete matkul dari graph karena asumsi sudah diambil
        self.nodes.pop(todelete)
    
    #mengecek apakah semua matkul yang ada di graf
    #sudah memiliki in degree 0 untuk basis rekursi
    def checkAllZeroInDegree(self):
        i = 0
        while(i < len(self.nodes)):
            if(self.nodes[i].inDegree != 0):
                return False
            i += 1
        return True


#membuat objek graph
graeph = graph()
#membuka file
namafile = input("Masukkan nama file :")
file = open("../test/"+namafile, "r")
for c in file:
    #menghapus karakter yang tidak perlu
    node = c.replace(' ','').replace('.','').replace('\n','').split(",")
    #memasukkan node matkul ke dalam graph
    graeph.addNode(matkul(node))

#Decrease and conquer
def topoSort(graf, sem):
    #basis
    if(graf.checkAllZeroInDegree()):
        #Mengeprint semua matkul karena semua inDegree sudah 0
        print("Semester ",sem,"\t:",end='')
        for i in graf.nodes:
            print(i.name, end = ', ')
        print("\b\b",end='')
        print(" ")
        
    #rekurens
    else:
        #inisialisasi dan cetak "Semester"
        i = 0
        todelete = graph()
        print("Semester ",sem,"\t:",end='')

        #mencetak matkul yang memiliki inDegree 0
        while(i<len(graf.nodes)):
            if(graf.nodes[i].inDegree == 0):
                print(graf.nodes[i].name, end=', ')
                #pencatatan matkul ke todelete jika
                #inDegree 0 karena matkul akan didelete
                todelete.addNode(graf.nodes[i])
            i += 1
        print("\b\b",end='')
        print(" ")

        #mendelete semua matkul yang ada dalam todelete
        for d in todelete.nodes:
            graf.popNode(d)
        
        #pemanggilan fungsi rekursi dengan graf baru yang ukurannya telah didecrease
        #variabel "sem" untuk menunjukkan nomor semester
        topoSort(graf,sem+1)

#pemanggilan fungsi
topoSort(graeph,1)