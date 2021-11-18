from PyPDF2 import PdfFileMerger
import PySimpleGUI as sg

def merge_pdfs(pdfs: list, out_name: str):
    """Takes the PDF documents, whose file paths are in list, and merges them to one PDF document. The resulting document is saved with the name out_name.
    
    :param pdfs: list of file paths to PDF documents
    :param out_name: the name of the resulting PDF document
    """
    merger = PdfFileMerger()
    
    for pdf in pdfs:
        merger.append(pdf)
    
    merger.write(out_name)
    merger.close()

def main():
    sg.theme("SystemDefaultForReal")
    
    pdfs = []
    
    col1 = [[sg.Text("Wähle eine Datei:"), sg.Input(), sg.FileBrowse(key="-IN-")],
              [sg.Button("Datei hinzufügen")]]
    col2 = [[sg.Listbox(values=pdfs, size=(100, 10), key="-LIST-", enable_events=True, select_mode="LISTBOX_SELECT_MODE_SINGLE")],
            [sg.Button("Datei entfernen")],
            [sg.Text("Name der Augabe-Datei:"), sg.Input(key="-OUTNAME-"), sg.Button("Datei speichern")]]

    layout = [[sg.Column(col1), sg.VSeperator(), sg.Column(col2)]]

    window = sg.Window("PDFmerger", layout).Finalize()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "Datei hinzufügen":
            pdfs.append(values["-IN-"])
            window["-LIST-"].update(values=pdfs)
            window.refresh()
        elif event == "Datei speichern":
            merge_pdfs(pdfs, values["-OUTNAME-"])
        elif event == "Datei entfernen":
            pdf_del = window["-LIST-"].get()
            pdfs.remove(pdf_del[0])
            window["-LIST-"].update(values=pdfs)
            window.refresh()


if __name__ == "__main__":
    main()
    
