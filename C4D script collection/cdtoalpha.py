import c4d
from c4d import gui

def main():
    doc.StartUndo()
    selectedMaterials = doc.GetActiveMaterials()
    for mat in selectedMaterials:
        if mat[c4d.MATERIAL_COLOR_SHADER] is not None:
            texture = mat[c4d.MATERIAL_COLOR_SHADER].GetClone()
            filterShader = c4d.BaseShader(c4d.Xfilter)
            filterShader[c4d.SLA_FILTER_SATURATION] = -1
            filterShader[c4d.SLA_FILTER_TEXTURE] = texture
            filterShader.InsertShader(texture)
            mat[c4d.MATERIAL_ALPHA_SHADER] = filterShader
            mat.InsertShader(filterShader)
            if mat[c4d.MATERIAL_USE_REFLECTION]:
                mat[c4d.MATERIAL_USE_REFLECTION] = False

    doc.EndUndo()
    c4d.EventAdd()

if __name__=='__main__':
    main()
