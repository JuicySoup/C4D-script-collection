import c4d
from c4d import gui

def collectShaders(tx, shaders):
    while tx:
        shaders.append(tx)
        if(tx.GetDown()): collectShaders(tx.GetDown(), shaders)
        tx=tx.GetNext()

def main():
    doc.StartUndo()
    #Get material selection
    mats = doc.GetActiveMaterials()

    # for each material in the selection collect
    for m in mats:
        shaders=[]
        collectShaders(m.GetFirstShader(), shaders)
        #Get each node in collection
        for node in shaders:
            if node.GetName() == "ColorCorrection":
                node.Remove()

    gui.MessageDialog("Done"); 
    doc.EndUndo()
    c4d.EventAdd()
if __name__=='__main__':
    main()
