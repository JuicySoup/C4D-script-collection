import c4d
import os

def main():
    
    doc.StartUndo()
    
    materials = doc.GetMaterials()
    for mat in materials:
        colorShader = mat[c4d.MATERIAL_COLOR_SHADER]
        if colorShader and colorShader.GetType() == c4d.Xbitmap:
            fullPath = colorShader[c4d.BITMAPSHADER_FILENAME]
            if "tex" in fullPath:
                 newPath = fullPath[6:]
                 doc.AddUndo(c4d.UNDOTYPE_CHANGE, mat)
                 colorShader[c4d.BITMAPSHADER_FILENAME] = newPath
            
    doc.EndUndo()
    c4d.EventAdd()


if __name__=='__main__':
    main()