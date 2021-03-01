import c4d
import os

def main():
    
    doc.StartUndo()
    
    # get all materials from the current active document
    # and iterate over them
    materials = doc.GetMaterials()
    for mat in materials:
        # get the color shader,
        # checks if one is assigned and if it is a texture
        colorShader = mat[c4d.MATERIAL_COLOR_SHADER]
        if colorShader and colorShader.GetType() == c4d.Xbitmap:
            # extract the filename from the shader
            fullPath = colorShader[c4d.BITMAPSHADER_FILENAME]
            if "/.tex/" in fullPath:
                fullPath = fullPath[6:]

            # rename the material
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, mat)
            mat.SetName(fullPath)
            
    doc.EndUndo()
    c4d.EventAdd()


if __name__=='__main__':
    main()
