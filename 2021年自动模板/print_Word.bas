Attribute VB_Name = "Ä£¿é1"
Function print_Word(files_arr, print_times As Integer, printer As String)
    On Error GoTo Err_cmdExportToWord_Click
    Set objApp = CreateObject("Word.Application")
    objApp.Visible = False
    objApp.ActivePrinter = printer
    For i = 1 To print_times
        For Each file In files_arr
            Set objDoc = objApp.Documents.Open(file, , False)
            objDoc.PrintOut
            objDoc.Close
        Next file
    Next i
    Set objApp = Nothing
    Set objDoc = Nothing
Exit_cmdExportToWord_Click:
        If Not objDoc Is Nothing Then objApp.Visible = True
        Set objApp = Nothing
        Set objDoc = Nothing
        Exit Function
Err_cmdExportToWord_Click:
        MsgBox Err.Description, vbCritical, "³ö´í"
        Resume Exit_cmdExportToWord_Click
End Function

