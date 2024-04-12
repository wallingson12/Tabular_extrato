import pandas as pd
import camelot

def extrair_tabelas_para_excel(pdf_file):
    tabelas = camelot.read_pdf(pdf_file, pages='all', flavor='stream')

    nome_arquivo = os.path.splitext(os.path.basename(pdf_file))[0]
    df_final = pd.DataFrame()

    for tabela in tabelas:
        df_final = pd.concat([df_final, tabela.df], ignore_index=False)

    output_dir = os.path.join(os.path.dirname(pdf_file), nome_arquivo)
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, f'{nome_arquivo}.xlsx')
    df_final.to_excel(output_file, header=False, index=False)

def processar_pdfs(pasta_origem):
    for root, dirs, files in os.walk(pasta_origem):
        for file in files:
            if file.endswith(".pdf"):
                pdf_file = os.path.join(root, file)
                extrair_tabelas_para_excel(pdf_file)
