estudiantes = ["juana", "sergio", "marcos", "keiner", "xavi", "adriana"]
estudiantes.append("camila")
print(estudiantes) #['juana', 'sergio', 'marcos', 'keiner', 'xavi', 'adriana', 'camila']
estudiantes.append("mateo")
print(estudiantes) #['juana', 'sergio', 'marcos', 'keiner', 'xavi', 'adriana', 'camila', 'mateo']
estudiantes.append("santiago")
print(estudiantes) #['juana', 'sergio', 'marcos', 'keiner', 'xavi', 'adriana', 'camila', 'mateo', 'santiago']
estudiantes.append("valentina")
print(estudiantes) #['juana', 'sergio', 'marcos', 'keiner', 'xavi', 'adriana', 'camila', 'mateo', 'santiago', 'valentina']
print(len(estudiantes)) #10
if "sergio" in estudiantes:
    print("sergio esta en la lista de estudiantes") #sergio esta en la lista de estudiantes
    estudiantes.remove("sergio")
print(estudiantes) #['juana', 'marcos', 'keiner', 'xavi', 'adriana', 'camila', 'mateo', 'santiago', 'valentina']