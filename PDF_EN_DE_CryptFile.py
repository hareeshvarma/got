import fitz

# def is_encrypted(file):
#     pdf = fitz.Document(file)
#     return pdf.isEncrypted

# file = 'Info_Protected_PDF.pdf'
# # print(is_encrypted(file))
# if is_encrypted(file):
#     password = input('Enter the password : ')
#     pdf = fitz.open(file)
#     if pdf.authenticate(password):
#         # page = pdf.loadpage(1)
#         # print(page.getText('text'))
#         pdf.save('unprotect.pdf')
#     else:
#         print('Incorrect password')

#encrypted logic

def encrypt_pdf(pdf,password,outfile):
    perm = int(
                fitz.PDF_PERM_ACCESSIBILITY
                | fitz.PDF_PERM_PRINT
                | fitz.PDF_PERM_COPY
                | fitz.PDF_PERM_ANNOTATE
                )
    encrypt_meth = fitz.PDF_ENCRYPT_AES_256
    pdf.save(outfile,encryption = encrypt_meth,user_pw = password, permissions=perm)

file = 'unprotect.pdf'
pdf = fitz.open(file)
encrypt_pdf(pdf,'123456','encrypt_Logic.pdf')