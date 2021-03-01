import c4d

def rename(obj):
  texture_tag = obj.GetTag(c4d.Ttexture)
  if not texture_tag: return
  
  mat = texture_tag[c4d.TEXTURETAG_MATERIAL]
  if not mat: return
  
  name = "{}".format(mat.GetName() - ".tif") 
  
  doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)
  obj.SetName(name)

def iter_hierarchy(obj):
  while obj:
    rename(obj)
    iter_hierarchy(obj.GetDown())
    obj = obj.GetNext()

def main():
    doc = c4d.documents.GetActiveDocument()
    if not doc: return
    
    doc.StartUndo()
    iter_hierarchy(doc.GetFirstObject())
    doc.EndUndo()
    c4d.EventAdd()
    
if __name__=='__main__':
    main()