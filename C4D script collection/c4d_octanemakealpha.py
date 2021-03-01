import c4d
from c4d import gui

ID_OCTANE_IMAGE_TEXTURE = 1029508

def collectShaders(tx, shaders):
    if shaders is None:
        shaders = []
    while tx:
        shaders.append(tx)
        if tx.GetDown():
            collectShaders(tx.GetDown(), shaders)
        tx=tx.GetNext()
    return shaders

def getName(node, name):
    if node.GetName() == name:
        name = node
    return name

def first(mats):
    # for each material in the selection collect
    for m in mats:
        try:
            m[c4d.OCT_MATERIAL_OPACITY_LINK].GetName()
        except AttributeError:
            pass
        else:
            if m[c4d.OCT_MATERIAL_OPACITY_LINK].GetName() == "ImageTexture":
                continue
        shaders = None
        shaders = collectShaders(m.GetFirstShader(), shaders)
        #Get each node in collection
        for node in shaders:
            if node.GetName() == "ImageTexture":
                diffuse = getName(node, "ImageTexture")
                continue
            elif node.GetName() == "ColorCorrection":
                if node.GetDown() in shaders:
                    shaders.remove(node.GetDown())
                node.GetDown().Remove()
                node.Remove()
        
        opacity = c4d.BaseShader(ID_OCTANE_IMAGE_TEXTURE)
        m.InsertShader(opacity)
        m[c4d.OCT_MATERIAL_OPACITY_LINK] = opacity
        opacity[c4d.IMAGETEXTURE_FILE] = diffuse[c4d.IMAGETEXTURE_FILE]
        opacity[c4d.IMAGETEXTURE_MODE] = 2
        
def main():
    doc.StartUndo()
    mats = doc.GetActiveMaterials()
    first(mats)
    gui.MessageDialog("Done"); 
    doc.EndUndo()
    c4d.EventAdd()

if __name__=='__main__':
    main()