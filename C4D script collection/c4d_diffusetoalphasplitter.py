import c4d
from c4d import gui
from RedshiftWrapper.Redshift import Redshift

def main():
    doc.StartUndo()
    rs = Redshift()
    if rs is False: return

    selectedMaterials = doc.GetActiveMaterials()
    for mat in selectedMaterials:
        rs.SetMat(mat)

        listNode = rs.GetAllNodes()
        for node in listNode:
            if node.GetName() == "Alpha Splitter":
                AlphaSplitter = node
            elif node.GetName() == "Diffuse":
                Diffuse = node
            elif node.GetName() == "Alpha":
                Alpha = node
        if not 'Alpha' in locals():
            return

        port = Alpha.SearchPort("Out Color")
        rs.RemoveConnection(port, Alpha, c4d.GV_PORT_INPUT)
        AlphaSplitter.ExposeParameter(c4d.REDSHIFT_SHADER_RSCOLORSPLITTER_INPUT, c4d.GV_PORT_INPUT)
        rs.CreateConnection(Diffuse, AlphaSplitter, 0,0)
        print "Connection"

    doc.EndUndo()
    c4d.EventAdd()

if __name__=='__main__':
    main()